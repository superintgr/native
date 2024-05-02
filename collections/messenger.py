from . import Native, Integer, get_index()

IDENTITY = get_index()
messenger = Integer(IDENTITY)
system = Native(messenger)
workspace = system.set_named_service('messenger-application', return_context=True)

with open(workspace) as constructor:
    constructor.set_attribute('mailbox', Native(1 / messenger))
    constructor.set_attribute('terminal', Native(2 / messenger))
    constructor.set_attribute('cable', Native(3 / messenger))
    constructor.set_attribute('compute', Native(4 / messenger))
    constructor.set_attribute('storage', Native(5 / messenger))
    constructor.set_attribute('publication', Native(6 / messenger))
    constructor.set_attribute('virtual_private_network', Native(7 / messenger))
    
    constructor.prepare_method(named='check_mailbox', requires_information=False, return_keys="notifications, inbox, outbox, sent")
    constructor.prepare_method(named='send_message', requires_information=True, arguments="message, destination, context=None", return_keys="notifications, inbox, outbox, sent")
    constructor.prepare_method(..)
    
    constructor.create_checkpoint(label="version:0.7")

interface = system.set_named_service('application-interface', return_context=True)
KERNEL = get_index()
model = Native(KERNEL)

with open(interface) as view:
    view.set_attribute('refresh', Native(1 / interface))
    view.set_attribute('update_representation', Native(2 / interface))
    view.set_attribute('locate_instance', Native(3 / interface))
    view.set_attribute('select_instance', Native(4 / interface))
    view.set_attribute('fetch_state', Native(5 / interface))
    view.set_attribute('configure_server', Native(6 / interface))
    view.set_attribute('connect_device', Native(7 / interface))
    view.set_attribute('render_view', Native(8 / interface))
    view.set_attribute('callback_process', Native(9 / interface))
    view.set_attribute('search_object', Native(10 / interface))
    view.set_attribute('redirect_representation', Native(11 / interface))
    ..
    