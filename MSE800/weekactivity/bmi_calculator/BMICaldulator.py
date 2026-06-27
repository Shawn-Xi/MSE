from flask import Flask, render_template_string


app = Flask(__name__)


@app.route("/api/name/<name>")
def get_name(name):
    return name


@app.route("/")
def home():
    return bmi("Guest")


@app.route("/BMI")
def bmi_default():
    return bmi("Guest")


@app.route("/BMI/<name>")
def bmi(name):
    return render_template_string(
        """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>BMI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f5f7fb;
            color: #1f2937;
        }

        main {
            max-width: 420px;
            margin: 0 auto;
            padding: 24px;
            background: white;
            border: 1px solid #d9e2ec;
            border-radius: 8px;
        }

        label {
            display: block;
            margin-top: 16px;
            font-weight: bold;
        }

        input {
            box-sizing: border-box;
            width: 100%;
            margin-top: 6px;
            padding: 10px;
            border: 1px solid #b8c2cc;
            border-radius: 4px;
            font-size: 16px;
        }

        button {
            width: 100%;
            margin-top: 20px;
            padding: 11px;
            border: 0;
            border-radius: 4px;
            background: #2563eb;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }

        #result {
            margin-top: 20px;
            font-size: 18px;
            line-height: 1.5;
        }

        .error {
            color: #b91c1c;
        }
    </style>
</head>
<body>
    <main>
        <h1>BMI</h1>

        <label for="weight">Weight in kilograms</label>
        <input id="weight" type="number" min="1" step="0.1" required>

        <label for="height">Height in meters</label>
        <input id="height" type="number" min="0.1" step="0.01" required>

        <button type="button" id="calculate">calculator</button>

        <div id="result"></div>
    </main>

    <script>
        const userNameFromPath = "{{ name }}";

        function classifyBmi(bmi) {
            if (bmi < 18.5) {
                return "thin";
            }
            if (bmi < 25) {
                return "normal";
            }
            return "fat";
        }

        document.getElementById("calculate").addEventListener("click", async () => {
            const weight = Number(document.getElementById("weight").value);
            const height = Number(document.getElementById("height").value);
            const result = document.getElementById("result");

            if (!weight || !height || weight <= 0 || height <= 0) {
                result.className = "error";
                result.textContent = "Please enter a valid weight and height.";
                return;
            }

            const response = await fetch(`/api/name/${encodeURIComponent(userNameFromPath)}`);
            const name = await response.text();
            const bmi = weight / (height * height);
            const classification = classifyBmi(bmi);

            result.className = "";
            result.innerHTML = `${name}, your BMI is: ${bmi.toFixed(2)}<br>You are classified as: ${classification}`;
        });
    </script>
</body>
</html>
        """,
        name=name,
    )


if __name__ == "__main__":
    app.run(debug=True)
