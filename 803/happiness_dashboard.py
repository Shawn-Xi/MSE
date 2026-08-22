from pathlib import Path

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


DATA_FILE = Path(__file__).with_name('world_happiness_dataset.csv')


def load_dataset():
    df = pd.read_csv(DATA_FILE)
    required = {'Country', 'Happiness_Score', 'Freedom_to_Make_Choices'}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")
    return df


def top_three_happiest(df):
    return df.nlargest(3, 'Happiness_Score')[['Country', 'Happiness_Score']].reset_index(drop=True)


def lowest_happiness_country(df):
    return df.nsmallest(1, 'Happiness_Score').iloc[0]


def build_matplotlib_top_three(top_three):
    fig, ax = plt.subplots(figsize=(9, 6))
    colors = ['#4C78A8', '#F58518', '#54A24B']
    bars = ax.bar(top_three['Country'], top_three['Happiness_Score'], color=colors)
    ax.set_title('Top 3 Happiest Countries', fontsize=14, fontweight='bold')
    ax.set_xlabel('Country')
    ax.set_ylabel('Happiness Score')
    ax.set_ylim(0, max(top_three['Happiness_Score']) + 1)

    for bar, value in zip(bars, top_three['Happiness_Score']):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.08, f'{value:.2f}', ha='center', va='bottom')

    plt.tight_layout()
    return fig


def build_plotly_top_three(top_three):
    fig = px.bar(
        top_three,
        x='Country',
        y='Happiness_Score',
        color='Country',
        text='Happiness_Score',
        title='Top 3 Happiest Countries',
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(xaxis_title='Country', yaxis_title='Happiness Score')
    return fig


def build_matplotlib_freedom_summary(lowest_row, df):
    summary = pd.DataFrame(
        {
            'Metric': ['Lowest Happiness Country', 'Dataset Mean', 'Dataset Median'],
            'Freedom_to_Make_Choices': [
                lowest_row['Freedom_to_Make_Choices'],
                df['Freedom_to_Make_Choices'].mean(),
                df['Freedom_to_Make_Choices'].median(),
            ],
        }
    )

    fig, ax = plt.subplots(figsize=(9, 6))
    colors = ['#E45756', '#B0B0B0', '#B0B0B0']
    bars = ax.barh(summary['Metric'], summary['Freedom_to_Make_Choices'], color=colors)
    ax.set_title(f"Freedom Score Summary for {lowest_row['Country']}", fontsize=14, fontweight='bold')
    ax.set_xlabel('Freedom to Make Choices')
    ax.set_ylabel('Metric')

    for bar, value in zip(bars, summary['Freedom_to_Make_Choices']):
        ax.text(value + 0.02, bar.get_y() + bar.get_height() / 2, f'{value:.2f}', va='center')

    plt.tight_layout()
    return fig


def build_plotly_freedom_summary(lowest_row, df):
    summary = pd.DataFrame(
        {
            'Metric': ['Lowest Happiness Country', 'Dataset Mean', 'Dataset Median'],
            'Freedom_to_Make_Choices': [
                lowest_row['Freedom_to_Make_Choices'],
                df['Freedom_to_Make_Choices'].mean(),
                df['Freedom_to_Make_Choices'].median(),
            ],
        }
    )
    fig = px.bar(
        summary,
        x='Freedom_to_Make_Choices',
        y='Metric',
        orientation='h',
        color='Metric',
        text='Freedom_to_Make_Choices',
        title=f"Freedom Score Summary for {lowest_row['Country']}",
        color_discrete_sequence=['#E45756', '#A0A0A0', '#A0A0A0'],
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(xaxis_title='Freedom to Make Choices', yaxis_title='Metric')
    return fig


def main():
    df = load_dataset()
    top_three = top_three_happiest(df)
    lowest_row = lowest_happiness_country(df)

    print('Top 3 happiest countries:')
    print(top_three.to_string(index=False))
    print('\nLowest happiness country:')
    print(
        f"{lowest_row['Country']} | Happiness Score = {lowest_row['Happiness_Score']:.2f} | "
        f"Freedom Score = {lowest_row['Freedom_to_Make_Choices']:.2f}"
    )

    output_dir = DATA_FILE.parent

    # Matplotlib outputs
    top_three_fig = build_matplotlib_top_three(top_three)
    top_three_fig.savefig(output_dir / 'top_three_happiness_matplotlib.png', dpi=200, bbox_inches='tight')

    freedom_fig = build_matplotlib_freedom_summary(lowest_row, df)
    freedom_fig.savefig(output_dir / 'lowest_country_freedom_matplotlib.png', dpi=200, bbox_inches='tight')

    # Plotly outputs
    top_three_plotly = build_plotly_top_three(top_three)
    top_three_plotly.write_html(str(output_dir / 'top_three_happiness_plotly.html'))

    freedom_plotly = build_plotly_freedom_summary(lowest_row, df)
    freedom_plotly.write_html(str(output_dir / 'lowest_country_freedom_plotly.html'))

    print('\nSaved charts:')
    print(f' - {output_dir / "top_three_happiness_matplotlib.png"}')
    print(f' - {output_dir / "lowest_country_freedom_matplotlib.png"}')
    print(f' - {output_dir / "top_three_happiness_plotly.html"}')
    print(f' - {output_dir / "lowest_country_freedom_plotly.html"}')


if __name__ == '__main__':
    main()



# Findings: • Top 3 happiest: Canada (7.34), Brazil (6.98), Finland (6.67) • Lowest happiness: South Africa (3.53) •
# Freedom score for South Africa: 0.90
# Why bar charts are best here: • The data is categorical (countries) and
# numeric (scores), so a bar chart makes country-to-country comparison immediate and easy to read. • A horizontal bar
# chart is especially useful for the Freedom summary because it compares one target value against the dataset
# mean/median clearly.