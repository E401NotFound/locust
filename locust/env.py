from .event import Events


class Environment:
    events = None
    """
    Event hooks used by Locust internally, as well as to extend Locust's functionality
    See :ref:`events` for available events.
    """
    
    runner = None
    """Reference to the LocustRunner instance"""
    
    web_ui = None
    """Reference to the WebUI instance"""
    
    options = None
    """Parsed command line options"""
    
    host = None
    """Base URL of the target system"""
    
    reset_stats = False
    """Determines if stats should be reset once all simulated users have been spawned"""
    
    step_load = False
    """Determines if we're running in step load mode"""
    
    stop_timeout = None
    """
    If set, the runner will try to stop the runnning users gracefully and wait this many seconds 
    before killing them hard.
    """
    
    catch_exceptions = True
    """
    If True exceptions that happen within running users will be catched (and reported in UI/console).
    If False, exeptions will be raised.
    """
    
    def  __init__(
        self, 
        events=None, 
        options=None, 
        host=None, 
        reset_stats=False, 
        step_load=False, 
        stop_timeout=None,
        catch_exceptions=True,
    ):
        if events:
            self.events = events
        else:
            self.events = Events()
        
        self.options = options
        self.host = host
        self.reset_stats = reset_stats
        self.step_load = step_load
        self.stop_timeout = stop_timeout
        self.catch_exceptions = catch_exceptions
        
