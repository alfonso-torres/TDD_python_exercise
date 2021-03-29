# TDD (Test Driven Development) EXERCISE - PYTHON

## <u>Exercise 1: TDD Bread Factory!</u>

TDD bread factory is the latest bread brand in Py Land. It always produces the best bread because it has the best testing strategy! What they do is before they make any new bread, they make a test to make sure the end ouput is correct. Then they adjust the recipe until it's just right!
You are going to do the same with bread! This is called Test Driven Development.

***__Tasks__***:

This exercise is going to bring together lots of concepts.

- Learning outcomes:
1. git
2. github
3. functions
4. TDD
5. Separation of concerns - this is important do not ignore!
6. DRY code
7. DOD
- Installing and running:

To run the naan factory do the following:
````python
import naan_factory
run_factory()
````
- TDD - test driven developmeent:
1. Write the test
2. Run it, and read the error
3. Code and make it pass the test

This helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write unit tests.

- Unit Test:

Test single pieces of code. Like a function.<br/>
Base of a test, usually has 3 phases:
1. setup phase (know variables)
2. calling of the function / piece of code with know variables
3. asserting for expect output

- User stories for Naan Factory:
1. As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.
2. As a user, I can use the bake dough with dough to get naan.
3. As a user, I can use the run factory with water and flour and get naan.

***__Acceptance Criteria__***:

- You have written tests.
- Test pass.
- You have written more test to make sure everything works as indented.
- All user stories are satisfied.
- Code does not break.
- Code has exit condition.
- DOD if followed.
