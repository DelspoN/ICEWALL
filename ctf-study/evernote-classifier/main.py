#-*- coding: utf-8 -*-

from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore

from config import authToken, writeupGuid
import re

def parseNoteInfo(noteTitle):
  noteTitle = noteTitle.decode('utf-8')
  info = dict()

  # title form : [{name}]/{title}
  formatChars = ['[', ']', '/']

  if len(noteTitle) < 5:
    return info
  for c in formatChars:
    if c not in noteTitle:
      return info

  name  = noteTitle.split('[')[1].split(']')[0].strip()
  title = noteTitle.split('/')[1].strip()

  info['name']  = name.encode('utf-8')
  info['title'] = title.encode('utf-8')
  return info

def main():
  client = EvernoteClient(token=authToken,sandbox=False)

  noteStore = client.get_note_store()

  filter = NoteStore.NoteFilter()
  filter.notebookGuid = writeupGuid

  spec = NoteStore.NotesMetadataResultSpec()
  spec.includeTitle = True

  ourNoteList = noteStore.findNotesMetadata(authToken, filter, 0, 100, spec)
  for note in ourNoteList.notes:
    info = parseNoteInfo(note.title)
    if len(info) != 0:
      print "%s :: %s" % (info['name'], info['title'])

if __name__ == '__main__': 
  main()
