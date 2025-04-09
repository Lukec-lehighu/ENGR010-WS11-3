from my_module import Chooser, gen_plot, print_rect

def test_chooser():
    assert Chooser([1,]).select() == 1

def test_gen_plot():
    assert gen_plot(lambda x: x, 'test', [1, 2, 3]) #returns true if function ran successfully

def test_print_rect():
    assert print_rect(5) #returns true if function ran successfully