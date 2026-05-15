a decorator is a function which is used to add some extra logic to a function. Before and after.
Take function student_login as an example, it's assigned by "log_activity", and function/decorator is defined in file decorators.py.
So in the function body I can see some extra logic before the original fun is executed. print some logs.
Then the exactly function student_login is executed, it's passed to the decorator as an argument - fun.
after it's executed, more logs are printed.