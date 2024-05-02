from . import Native, Integer, get_index()

IDENTITY = get_index()

messenger = Integer(IDENTITY)
system = Native(messenger)

workspace = system.set_named_service('messenger-application', return_context=True)

with open(workspace) as constructor:
    constructor.set_attribute('mailbox', Native(system))
    constructor.set_attribute('terminal', Native(system))
    constructor.set_attribute('cable', Native(system))
    constructor.set_attribute('compute', Native(system))
    constructor.set_attribute('storage', Native(system))
    constructor.set_attribute('publication', Native(system))
    constructor.set_attribute('virtual_private_network', Native(system))
    
    constructor.prepare_method(named='check_mailbox', requires_information=False, return_keys="notifications, inbox, outbox, sent")
    constructor.prepare_method(named='send_message', requires_information=True, arguments="message, destination, context=None", return_keys="notifications, inbox, outbox, sent")
    constructor.prepare_method(..)
    
    constructor.create_checkpoint(label="version:0.2")

