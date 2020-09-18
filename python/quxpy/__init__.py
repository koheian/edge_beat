try:
    from .quxpy import metro
    from .quxpy import osc_receiver
    from .quxpy import osc_sender
    from .quxpy import process_event
    from .quxpy import thread_event
except ModuleNotFoundError:
    print(" Some modules does not work because the dependencies are not installed collectly.")