"""The phonological loop comprises a phonological store that is dedicated to working memory and that serves to temporarily hold verbal information, and an articulatory loop, through which inner speech is used to reactivate, or “refresh,” the representations in the phonological store."""

generic = default_graph(vocab=17448, keys=1048, paths=408, directed=False)

scetch = {
    repr : {
        Master : (memory, regular),
        other : information
    },
    information : {
        Master : (art, memory),
        other : repr),
    },
    regular : {
        Observer : (),
        orher : articulatory loop,
    },
    art : {
        Observer : (),
        other : articulatory loop,
    },
    store : {
        Observer : (),
        other : memory,
    },
    memory : {
        Master : (loop, store),
        other : dedicated working memory,
    },
    phonon : {
        Observer : (),
        other : phonological loop,
    },
    logic : {
        Observer : (),
        other : phonological loop,
    },
    loop : {
        Master : (phonon, logic),
        other : phonological loop,
    },
}


def load_graph(config):
    model = load(config)
    try:
        generic.scan_keys(model)
    except Exception as e:
        errors = generic.get_errors()
        if e in errors:
            errors.append(e) # this is temporary now
        else:
            generic.set_errors([e])
        return e

def extend_graph(active_model, transfer_node, callable, endpoint_model):
    active_model.add_node(transfer_node)
    active_model.add_link(callable, endpoint_model)
    active_model.add_edge_from(callable, transfer_node)

def search_node(name, directory, filter):
    for node in directory:
        scope = filter(node)
        if scope in node:
            try:
                edge = scope[name]
                yield edge
            except Exception as e:
                errors = directory.get_errors()
                if e in errors:
                    errors.append(e)
                else:
                    directory.set_error(e)

