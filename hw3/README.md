
# Introduce simple Makefile
- That creates three empty text files: “one”, “two”, “three”
	- Add tasks (with names “one”, “two” and “three”) that will create each of them
	- Each next task should depend on the result of previous, if “one” has been changed “two” and “three” should re-run
- Add task “all” that will create them one by one
- Add task “clear” that will drop them
	- Make sure that the task will run if if “clear” file will be created in folder
- Add alias task “other_one” that will do the same as “one”
	- But will also output the name of task: “other_one”
	- Make sure that there is nothing else in output
