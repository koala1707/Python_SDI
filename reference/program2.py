#program 2
import program1
import main

print("Imported " + program1.__name__)

program1.name_out()

print(main.__name__)