from src.Tray import Tray 
from src.Bullet import Bullet 
from src.GaltonBoard import GaltonBoard 
from src.DropPolicies.DescriptiveDropPolicy import DescriptiveDropPolicy 

numberOfTrays = 0;
direction = "";
galtonBoard = None;

@given(u'I have 5 trays')
def step_impl(context):
    global numberOfTrays;
    numberOfTrays = 5;

@given(u'I have 2 trays')
def step_impl(context):
    global numberOfTrays;
    numberOfTrays = 2;

@given(u'the bullet will fall "right,left,right,left"')
def step_impl(context):
    direction = "right,left,right,left";

@given(u'the bullet will fall "right,right,right,right"')
def step_impl(context):
    direction = "right,right,right,right";

@given(u'the bullet will fall "right,right,right,left"')
def step_impl(context):
    direction = "right,right,right,left";

@given(u'the bullet will fall "left,left,left,left"')
def step_impl(context):
    global direction;
    direction = "left,left,left,left";

@given(u'the bullet will fall "left,left,left,right"')
def step_impl(context):
    direction = "left,left,left,right";

@then(u'The bullet should be in tray 2')
def step_impl(context):
    if galtonBoard.getTrays()[0].numberOfBullets() != 1:
        raise Exception("Bullet not in tray 2");

@given(u'the bullet will fall "left"')
def step_impl(context):
    direction = "left";

@when(u'I drop the bullet')
def step_impl(context):
    global galtonBoard;
    galtonBoard = GaltonBoard(Tray.listFromLength(numberOfTrays), Bullet.listFromLength(1), DescriptiveDropPolicy(direction));
    galtonBoard = galtonBoard.dropBullets();

@then(u'The bullet should be in tray 1')
def step_impl(context):
    if galtonBoard.getTrays()[0].numberOfBullets() != 1:
        raise Exception("Bullet not in tray 1");

@then(u'The bullet should be in tray 5')
def step_impl(context):
    if galtonBoard.getTrays()[0].numberOfBullets() != 1:
        raise Exception("Bullet not in tray 5");

@then(u'The bullet should be in tray 3')
def step_impl(context):
    if galtonBoard.getTrays()[0].numberOfBullets() != 1:
        raise Exception("Bullet not in tray 3");

@then(u'The bullet should be in tray 4')
def step_impl(context):
    if galtonBoard.getTrays()[0].numberOfBullets() != 1:
        raise Exception("Bullet not in tray 4");
