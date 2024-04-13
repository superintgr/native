"""The phonological loop comprises a phonological store that is dedicated to working memory and that serves to temporarily hold verbal information, and an articulatory loop, through which inner speech is used to reactivate, or “refresh,” the representations in the phonological store."""

# phonological loop
phonon = Observer()
logic = Observer()
loop = Master(phonon, logic)

# dedicated working memory
store = Observer()
memory = Master(loop, store)

# articulatory loop
art = Observer()
regular = Observer()
information = Master(art, memory)
repr = Master(memory, regular)
