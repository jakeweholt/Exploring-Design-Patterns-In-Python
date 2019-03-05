from state_machine import (State, Event, acts_as_state_machine,
                           after, before, InvalidStateTransition)
import time

 
@acts_as_state_machine 
class Process: 
    created = State(initial=True) 
    waiting = State() 
    moving_up = State()
    moving_down = State()
    opening_door = State()
    closing_door = State()
    blocked = State() 
    terminated = State() 
    
    wait = Event(from_states=(created, moving_up, moving_down, blocked, opening_door, closing_door), 
                 to_state=waiting)
    
    move_up = Event(from_states=waiting,
                    to_state=moving_up)
    
    move_down = Event(from_states=waiting,
                      to_state=moving_down)
    
    open_door = Event(from_states=waiting,
                      to_state=opening_door)
    
    close_door = Event(from_states=waiting,
                      to_state=closing_door)
    
    block = Event(from_states=(move_up, move_down),
                      to_state=blocked)
    
    terminate = Event(from_states=wait,
                      to_state=terminated)
    
    @after('wait') 
    def wait_info(self): 
        print '{} entered waiting mode at floor {}'.format(self.name, self.current_floor)
 
    @after('move_up') 
    def run_info(self): 
        print '{} is moving up from floor {} to floor {}'.format(self.name, self.current_floor, self.target_floor) 
        time.sleep(3)
        self.current_floor = self.target_floor
        
    @after('move_down') 
    def run_info(self): 
        print '{} is moving down from floor {} to floor {}'.format(self.name, self.current_floor, self.target_floor) 
        time.sleep(3)
        self.current_floor = self.target_floor
        
    @before('open_door') 
    def terminate_info(self): 
        print '{} door opening'.format(self.name)
        time.sleep(2)
        
    @before('close_door') 
    def terminate_info(self): 
        print '{} door closing'.format(self.name)
        time.sleep(2)
 
    @before('terminate') 
    def terminate_info(self): 
        print '{} terminated'.format(self.name)
 
    @after('block') 
    def block_info(self): 
        print '{} is blocked'.format(self.name)
    
    def __init__(self, name, current_floor=0): 
        self.name = name
        self.current_floor = current_floor
        self.target_floor = None
        
    def set_target_floor(self, target_floor):
        self.target_floor = target_floor
        
    def set_current_floor(self, current_floor):
        self.current_floor = current_floor
        
        
def transition(process, event, event_name): 
    try: 
        event() 
    except  InvalidStateTransition as err: 
        print('Error: transition of {} from {} to {} failed'.format(process.name, process.current_state, event_name))
        
def move_elevator(process, event, event_name, floor):
    e1.set_target_floor(floor)
    transition(process, event, event_name)
    transition(e1, e1.wait, WAITING)
    transition(e1, e1.open_door, OPENINGDOOR)
    transition(e1, e1.wait, WAITING)
    transition(e1, e1.close_door, CLOSINGDOOR)
    transition(e1, e1.wait, WAITING)