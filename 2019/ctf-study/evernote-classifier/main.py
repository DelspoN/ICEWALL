#-*- coding: utf-8 -*-

from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore
from evernote.edam.type import ttypes

from config import authToken, writeupGuid, noticeGuid

import datetime, json

def makeNote(authToken, noteStore, noteTitle, noteBody, parentNotebook=None):
  nBody = '<?xml version="1.0" encoding="UTF-8"?>'
  nBody += '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
  nBody += '<en-note>%s</en-note>' % noteBody.replace("\n", "<br />")

  ## Create note object
  ourNote = ttypes.Note()
  ourNote.title = noteTitle
  ourNote.content = nBody

  ## parentNotebook is optional; if omitted, default notebook is used
  if parentNotebook and hasattr(parentNotebook, 'guid'):
    ourNote.notebookGuid = parentNotebook.guid

  ## Attempt to create note in Evernote account
  try:
    note = noteStore.createNote(authToken, ourNote)
  except Errors.EDAMUserException, edue:
    ## Something was wrong with the note data
    ## See EDAMErrorCode enumeration for error code explanation
    ## http://dev.evernote.com/documentation/reference/Errors.html#Enum_EDAMErrorCode
    print "EDAMUserException:", edue
    return None
  except Errors.EDAMNotFoundException, ednfe:
    ## Parent Notebook GUID doesn't correspond to an actual notebook
    print "EDAMNotFoundException: Invalid parent notebook GUID"
    return None

  ## Return created note object
  return note

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

def getWriteupList(client, noteStore):
  writeupList = []

  # filter for writetup notebook
  filter = NoteStore.NoteFilter()
  filter.notebookGuid = writeupGuid

  spec = NoteStore.NotesMetadataResultSpec()
  spec.includeTitle = True

  ourNoteList = noteStore.findNotesMetadata(authToken, filter, 0, 1000, spec)
  for note in ourNoteList.notes:
    info = parseNoteInfo(note.title)
    info['guid'] = note.guid
    if len(info) != 0:
      writeupList.append(info)

  return writeupList

def main():
  client = EvernoteClient(token=authToken,sandbox=False)
  noteStore = client.get_note_store()
  writeupList = getWriteupList(client, noteStore)

  title = '[Scoreboard] %s' % str(datetime.datetime.now())
  content = json.dumps(writeupList)
  noticeNotebook = noteStore.getNotebook(noticeGuid)
  makeNote(authToken, noteStore, title, content, noticeNotebook)

if __name__ == '__main__': 
  main()
