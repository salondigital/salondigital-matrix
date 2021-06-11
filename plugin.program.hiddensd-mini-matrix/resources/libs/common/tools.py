import base64, codecs
magic = 'SU5TVEFMTF9QQUdFICAgICA9ICdodHRwOi8vc2Fsb25kaWdpdGFsLmVzL2NoZWNrLnBocCcNClVTRVJfQUdFTlQgICAJID0gJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdPVzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNDcuMC4yNTI2LjczIFNhZmFyaS81MzcuMzYgUmVwbGljYW50V2l6YXJkLzEuMC4wJw0KTUVNQkVSU19VUkwgICAgICA9ICdodHRwOi8vc2Fsb25kaWdpdGFsLmVzLycNCldJWkFSRF9QQUdFICAgICAgPSAnd2l6YXJkLnBocCcNCg0KaW1wb3J0IHhibWMNCmltcG9ydCB4Ym1jYWRkb24NCmltcG9ydCB4Ym1jZ3VpDQoNCmltcG9ydCBvcw0KaW1wb3J0IHJhbmRvbQ0KaW1wb3J0IHJlDQppbXBvcnQgc2h1dGlsDQppbXBvcnQgc3RyaW5nDQppbXBvcnQgc3lzDQpmcm9tIHJlc291cmNlcy5saWJzIGltcG9ydCB3aXphcmQgYXMgd2l6DQoNCmlmIHN5cy52ZXJzaW9uX2luZm9bMF0gPiAyOg0KICAgICMgUHl0aG9uIDMNCiAgICBwYXNzDQplbHNlOg0KICAgICMgUHl0aG9uIDINCiAgICBpbXBvcnQgY29kZWNzDQogICAgaW1wb3J0IHdhcm5pbmdzDQoNCiAgICBkZWYgb3BlbihmaWxlLCBtb2RlPSdyJywgYnVmZmVyaW5nPS0xLCBlbmNvZGluZz0ndXRmLTgnLCBlcnJvcnM9Tm9uZSwgbmV3bGluZT1Ob25lLCBjbG9zZWZkPVRydWUsIG9wZW5lcj1Ob25lKToNCiAgICAgICAgaWYgbmV3bGluZSBpcyBub3QgTm9uZToNCiAgICAgICAgICAgIHdhcm5pbmdzLndhcm4oJ25ld2xpbmUgaXMgbm90IHN1cHBvcnRlZCBpbiBweTInKQ0KICAgICAgICBpZiBub3QgY2xvc2VmZDoNCiAgICAgICAgICAgIHdhcm5pbmdzLndhcm4oJ2Nsb3NlZmQgaXMgbm90IHN1cHBvcnRlZCBpbiBweTInKQ0KICAgICAgICBpZiBvcGVuZXIgaXMgbm90IE5vbmU6DQogICAgICAgICAgICB3YXJuaW5ncy53YXJuKCdvcGVuZXIgaXMgbm90IHN1cHBvcnRlZCBpbiBweTInKQ0KICAgICAgICByZXR1cm4gY29kZWNzLm9wZW4oZmlsZW5hbWU9ZmlsZSwgbW9kZT1tb2RlLCBlbmNvZGluZz1lbmNvZGluZywgZXJyb3JzPWVycm9ycywgYnVmZmVyaW5nPWJ1ZmZlcmluZykNCg0KdHJ5OiAgIyBQeXRob24gMw0KICAgIGZyb20gdXJsbGliLnBhcnNlIGltcG9ydCBxdW90ZQ0KICAgIGZyb20gdXJsbGliLnBhcnNlIGltcG9ydCB1cmxwYXJzZQ0KICAgIGZyb20gaHRtbC5wYXJzZXIgaW1wb3J0IEhUTUxQYXJzZXINCmV4Y2VwdCBJbXBvcnRFcnJvcjogICMgUHl0aG9uIDINCiAgICBmcm9tIHVybGxpYiBpbXBvcnQgcXVvdGUNCiAgICBmcm9tIHVybHBhcnNlIGltcG9ydCB1cmxwYXJzZQ0KICAgIGltcG9ydCBIVE1MUGFyc2VyDQoNCmZyb20gY29udGV4dGxpYiBpbXBvcnQgY29udGV4dG1hbmFnZXINCg0KZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24uY29uZmlnIGltcG9ydCBDT05GSUcNCmltcG9ydCB1cmxsaWIucmVxdWVzdA0KDQoNCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiMgIEZpbGUgRnVuY3Rpb25zICAgICAgICMNCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCg0KZGVmIHJlYWRfZnJvbV9maWxlKGZpbGUsIG1vZGU9J3InKToNCiAgICBmID0gb3BlbihmaWxlLCBtb2RlLCBlbmNvZGluZz0ndXRmLTgnKQ0KICAgIGEgPSBmLnJlYWQoKQ0KICAgIGYuY2xvc2UoKQ0KICAgIHJldHVybiBhDQoNCmRlZiByZWFkX2Zyb21fZmlsZV9vbGQoZmlsZSwgbW9kZT0ncicpOg0KICAgIGYgPSBvcGVuKGZpbGUsIG1vZGUsIGVuY29kaW5nPU5vbmUpDQogICAgYSA9IGYucmVhZCgpDQogICAgZi5jbG9zZSgpDQogICAgcmV0dXJuIGENCg0KDQpkZWYgd3JpdGVfdG9fZmlsZShmaWxlLCBjb250ZW50LCBtb2RlPSd3Jyk6DQogICAgZiA9IG9wZW4oZmlsZSwgbW9kZSwgZW5jb2Rpbmc9J3V0Zi04JykNCiAgICBmLndyaXRlKGNvbnRlbnQpDQogICAgZi5jbG9zZSgpDQoNCg0KZGVmIHJlbW92ZV9mb2xkZXIocGF0aCk6DQogICAgZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24gaW1wb3J0IGxvZ2dpbmcNCg0KICAgIGxvZ2dpbmcubG9nKCJEZWxldGluZyBGb2xkZXI6IHswfSIuZm9ybWF0KHBhdGgpKQ0KICAgIHRyeToNCiAgICAgICAgc2h1dGlsLnJtdHJlZShwYXRoLCBpZ25vcmVfZXJyb3JzPVRydWUsIG9uZXJyb3I9Tm9uZSkNCiAgICBleGNlcHQ6DQogICAgICAgIHJldHVybiBGYWxzZQ0KDQoNCmRlZiByZW1vdmVfZmlsZShwYXRoKToNCiAgICBmcm9tIHJlc291cmNlcy5saWJzLmNvbW1vbiBpbXBvcnQgbG9nZ2luZw0KDQogICAgbG9nZ2luZy5sb2coIkRlbGV0aW5nIEZpbGU6IHswfSIuZm9ybWF0KHBhdGgpKQ0KICAgIHRyeToNCiAgICAgICAgb3MucmVtb3ZlKHBhdGgpDQogICAgZXhjZXB0Og0KICAgICAgICByZXR1cm4gRmFsc2UNCg0KDQpkZWYgZW1wdHlfZm9sZGVyKGZvbGRlcik6DQogICAgdG90YWwgPSAwDQogICAgZm9yIHJvb3QsIGRpcnMsIGZpbGVzIGluIG9zLndhbGsoZm9sZGVyLCB0b3Bkb3duPVRydWUpOg0KICAgICAgICBkaXJzWzpdID0gW2QgZm9yIGQgaW4gZGlycyBpZiBkIG5vdCBpbiBDT05GSUcuRVhDTFVERVNdDQogICAgICAgIGZpbGVfY291bnQgPSAwDQogICAgICAgIGZpbGVfY291bnQgKz0gbGVuKGZpbGVzKSArIGxlbihkaXJzKQ0KICAgICAgICBpZiBmaWxlX2NvdW50ID09IDA6DQogICAgICAgICAgICBzaHV0aWwucm10cmVlKG9zLnBhdGguam9pbihyb290KSkNCiAgICAgICAgICAgIHRvdGFsICs9IDENCg0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24gaW1wb3J0IGxvZ2dpbmcNCiAgICAgICAgICAgIGxvZ2dpbmcubG9nKCJFbXB0eSBGb2xkZXI6IHswfSIuZm9ybWF0KHJvb3QpKQ0KICAgIHJldHVybiB0b3RhbA0KDQoNCmRlZiBjbGVhbl9ob3VzZShmb2xkZXIsIGlnbm9yZT1GYWxzZSk6DQogICAgZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24gaW1wb3J0IGxvZ2dpbmcNCg0KICAgIGxvZ2dpbmcubG9nKGZvbGRlcikNCiAgICB0b3RhbF9maWxlcyA9IDANCiAgICB0b3RhbF9mb2xkcyA9IDANCiAgICBmb3Igcm9vdCwgZGlycywgZmlsZXMgaW4gb3Mud2Fsayhmb2xkZXIpOg0KICAgICAgICBpZiBub3QgaWdub3JlOg0KICAgICAgICAgICAgZGlyc1s6XSA9IFtkIGZvciBkIGluIGRpcnMgaWYgZCBub3QgaW4gQ09ORklHLkVYQ0xVREVTXQ0KICAgICAgICBmaWxlX2NvdW50ID0gMA0KICAgICAgICBmaWxlX2NvdW50ICs9IGxlbihmaWxlcykNCiAgICAgICAgaWYgZmlsZV9jb3VudCA+PSAwOg0KICAgICAgICAgICAgZm9yIGYgaW4gZmlsZXM6DQogICAgICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgICAgICBvcy51bmxpbmsob3MucGF0aC5qb2luKHJvb3QsIGYpKQ0KICAgICAgICAgICAgICAgICAgICB0b3RhbF9maWxlcyArPSAxDQogICAgICAgICAgICAgICAgZXhjZXB0Og0KICAgICAgICAgICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgICAgICAgICBzaHV0aWwucm10cmVlKG9zLnBhdGguam9pbihyb290LCBmKSkNCiAgICAgICAgICAgICAgICAgICAgZXhjZXB0Og0KICAgICAgICAgICAgICAgICAgICAgICAgbG9nZ2luZy5sb2coIkVycm9yIERlbGV0aW5nIHswfSIuZm9ybWF0KGYpLCBsZXZlbD14Ym1jLkxPR0VSUk9SKQ0KICAgICAgICAgICAgZm9yIGQgaW4gZGlyczoNCiAgICAgICAgICAgICAgICB0b3RhbF9mb2xkcyArPSAxDQogICAgICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgICAgICBzaHV0aWwucm10cmVlKG9zLnBhdGguam9pbihyb290LCBkKSkNCiAgICAgICAgICAgICAgICAgICAgdG90YWxfZm9sZHMgKz0gMQ0KICAgICAgICAgICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgICAgICAgICAgbG9nZ2luZy5sb2coIkVycm9yIERlbGV0aW5nIHswfSIuZm9ybWF0KGQpLCBsZXZlbD14Ym1jLkxPR0VSUk9SKQ0KICAgIHJldHVybiB0b3RhbF9maWxlcywgdG90YWxfZm9sZHMNCg0KDQpkZWYgY29weXRyZWUoc3JjLCBkc3QsIHN5bWxpbmtzPUZhbHNlLCBpZ25vcmU9Tm9uZSk6DQogICAgbmFtZXMgPSBvcy5saXN0ZGlyKHNyYykNCiAgICBpZiBpZ25vcmUgaXMgbm90IE5vbmU6DQogICAgICAgIGlnbm9yZWRfbmFtZXMgPSBpZ25vcmUoc3JjLCBuYW1lcykNCiAgICBlbHNlOg0KICAgICAgICBpZ25vcmVkX25hbWVzID0gc2V0KCkNCiAgICBpZiBub3Qgb3MucGF0aC5pc2Rpcihkc3QpOg0KICAgICAgICBvcy5tYWtlZGlycyhkc3QpDQogICAgZXJyb3JzID0gW10NCiAgICBmb3IgbmFtZSBpbiBuYW1lczoNCiAgICAgICAgaWYgbmFtZSBpbiBpZ25vcmVkX25hbWVzOg0KICAgICAgICAgICAgY29udGludWUNCiAgICAgICAgc3JjbmFtZSA9IG9zLnBhdGguam9pbihzcmMsIG5hbWUpDQogICAgICAgIGRzdG5hbWUgPSBvcy5wYXRoLmpvaW4oZHN0LCBuYW1lKQ0KICAgICAgICB0cnk6DQogICAgICAgICAgICBpZiBzeW1saW5rcyBhbmQgb3MucGF0aC5pc2xpbmsoc3JjbmFtZSk6DQogICAgICAgICAgICAgICAgbGlua3RvID0gb3MucmVhZGxpbmsoc3JjbmFtZSkNCiAgICAgICAgICAgICAgICBvcy5zeW1saW5rKGxpbmt0bywgZHN0bmFtZSkNCiAgICAgICAgICAgIGVsaWYgb3MucGF0aC5pc2RpcihzcmNuYW1lKToNCiAgICAgICAgICAgICAgICBjb3B5dHJlZShzcmNuYW1lLCBkc3RuYW1lLCBzeW1saW5rcywgaWdub3JlKQ0KICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICBzaHV0aWwuY29weTIoc3JjbmFtZSwgZHN0bmFtZSkNCiAgICAgICAgZXhjZXB0IEVudmlyb25tZW50RXJyb3IgYXMgd2h5Og0KICAgICAgICAgICAgZXJyb3JzLmFwcGVuZCgoc3JjbmFtZSwgZHN0bmFtZSwgc3RyKHdoeSkpKQ0KICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGVycjoNCiAgICAgICAgICAgIGVycm9ycy5leHRlbmQoZXJyLmFyZ3NbMF0pDQogICAgdHJ5Og0KICAgICAgICBzaHV0aWwuY29weXN0YXQoc3JjLCBkc3QpDQogICAgZXhjZXB0IE9TRXJyb3IgYXMgd2h5Og0KICAgICAgICBlcnJvcnMuZXh0ZW5kKChzcmMsIGRzdCwgc3RyKHdoeSkpKQ0KICAgIGlmIGVycm9yczoNCiAgICAgICAgcmFpc2UgRXhjZXB0aW9uDQoNCg0KZGVmIGZpbGVfY291bnQoaG9tZSwgZXhjbHVkZXM9VHJ1ZSk6DQogICAgaXRlbSA9IFtdDQogICAgZm9yIGJhc2UsIGRpcnMsIGZpbGVzIGluIG9zLndhbGsoaG9tZSk6DQogICAgICAgIGlmIGV4Y2x1ZGVzOg0KICAgICAgICAgICAgZGlyc1s6XSA9IFtkIGZvciBkIGluIGRpcnMgaWYgb3MucGF0aC5qb2luKGJhc2UsIGQpIG5vdCBpbiBDT05GSUcuRVhDTFVERV9ESVJTXQ0KICAgICAgICAgICAgZmlsZXNbOl0gPSBbZiBmb3IgZiBpbiBmaWxlcyBpZiBmIG5vdCBpbiBDT05GSUcuRVhDTFVERV9GSUxFU10NCiAgICAgICAgZm9yIGZpbGUgaW4gZmlsZXM6DQogICAgICAgICAgICBpdGVtLmFwcGVuZChmaWxlKQ0KICAgIHJldHVybiBsZW4oaXRlbSkNCiAgICANCg0KZGVmIGVuc3VyZV9mb2xkZXJzKGZvbGRlcj1Ob25lKToNCiAgICBpbXBvcnQgeGJtY3Zmcw0KDQogICAgbmFtZSA9ICcnDQogICAgZm9sZGVycyA9IFtDT05GSUcuQkFDS1VQTE9DQVRJT04sIENPTkZJRy5NWUJVSUxEUywgQ09ORklHLlBMVUdJTl9EQVRBLA0KICAgICAgICAgICAgICAgQ09ORklHLlVTRVJEQVRBLCBDT05GSUcuQURET05fREFUQSwgQ09ORklHLlBBQ0tBR0VTXQ0KDQogICAgdHJ5Og0KICAgICAgICBpZiBmb2xkZXIgaXMgbm90IE5vbmUgYW5kIG5vdCBvcy5wYXRoLmV4aXN0cyhmb2xkZXIpOg0KICAgICAgICAgICAgbmFtZSA9IGZvbGRlcg0KICAgICAgICAgICAgeGJtY3Zmcy5ta2RpcnMoZm9sZGVyKQ0KICAgICAgICAgICAgcmV0dXJuDQoNCiAgICAgICAgZm9yIGYgaW4gZm9sZGVyczoNCiAgICAgICAgICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhmKToNCiAgICAgICAgICAgICAgICBuYW1lID0gZg0KICAgICAgICAgICAgICAgIHhibWN2ZnMubWtkaXJzKGYpDQoNCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgICAgIGRpYWxvZyA9IHhibWNndWkuRGlhbG9nKCkNCg0KICAgICAgICBkaWFsb2cub2soQ09ORklHLkFERE9OVElUTEUsDQogICAgICAgICAgICAgICAgICAgICAgIltDT0xPUiB7MH1dRXJyb3IgY3JlYXRpbmcgYWRkLW9uIGRpcmVjdG9yaWVzOlsvQ09MT1JdIi5mb3JtYXQoQ09ORklHLkNPTE9SMikNCiAgICAgICAgICAgICAgICAgICAgICArJ1xuJysiW0NPTE9SIHswfV17MX1bL0NPTE9SXSIuZm9ybWF0KENPTkZJRy5DT0xPUjEsIG5hbWUpKQ0KICAgICAgICAgICAgICAgICAgICAgIA0KIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KIyAgVXRpbGl0eSBGdW5jdGlvbnMgICAgIw0KIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KDQoNCkBjb250ZXh0bWFuYWdlcg0KZGVmIGJ1c3lfZGlhbG9nKCk6DQogICAgeGJtYy5leGVjdXRlYnVpbHRpbignQWN0aXZhdGVXaW5kb3coYnVzeWRpYWxvZ25vY2FuY2VsKScpDQogICAgdHJ5Og0KICAgICAgICB5aWVsZA0KICAgIGZpbmFsbHk6DQogICAgICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ0RpYWxvZy5DbG9zZShidXN5ZGlhbG9nbm9jYW5jZWwpJykNCg0KDQpkZWYgY29udmVydF9zaX'
love = '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'
god = 'ICAgICAgIGxvZ2dpbmcubG9nKCJGb3JjZSBDbG9zaW5nIEtvZGk6IFBsYXRmb3JtW3swfV0iLmZvcm1hdChzdHIocGxhdGZvcm0oKSkpKQ0KICAgICAgICBvcy5fZXhpdCgxKQ0KDQoNCmRlZiByZWxvYWRfcHJvZmlsZShwcm9maWxlPU5vbmUpOg0KICAgIGlmIHByb2ZpbGUgaXMgTm9uZToNCiAgICAgICAgeGJtYy5leGVjdXRlYnVpbHRpbignTG9hZFByb2ZpbGUoTWFzdGVyIHVzZXIpJykNCiAgICBlbHNlOg0KICAgICAgICB4Ym1jLmV4ZWN1dGVidWlsdGluKCdMb2FkUHJvZmlsZSh7MH0pJy5mb3JtYXQocHJvZmlsZSkpDQoNCg0KZGVmIGNodW5rcyhzLCBuKToNCiAgICBmb3Igc3RhcnQgaW4gcmFuZ2UoMCwgbGVuKHMpLCBuKToNCiAgICAgICAgeWllbGQgc1tzdGFydDpzdGFydCtuXQ0KDQoNCmRlZiBjb252ZXJ0X3NwZWNpYWwodXJsLCBvdmVyPUZhbHNlKToNCiAgICBmcm9tIHJlc291cmNlcy5saWJzLmNvbW1vbiBpbXBvcnQgbG9nZ2luZw0KDQogICAgcHJvZ3Jlc3NfZGlhbG9nID0geGJtY2d1aS5EaWFsb2dQcm9ncmVzcygpDQogICAgDQogICAgdG90YWwgPSBmaWxlX2NvdW50KHVybCkNCiAgICBzdGFydCA9IDANCiAgICBwcm9ncmVzc19kaWFsb2cuY3JlYXRlKENPTkZJRy5BRERPTlRJVExFLCAiW0NPTE9SIHswfV1DaGFuZ2luZyBQaHlzaWNhbCBQYXRocyBUbyBTcGVjaWFsIi5mb3JtYXQoQ09ORklHLkNPTE9SMikgKyAiXG4iICsgIlBsZWFzZSBXYWl0Wy9DT0xPUl0iKQ0KICAgIGZvciByb290LCBkaXJzLCBmaWxlcyBpbiBvcy53YWxrKHVybCk6DQogICAgICAgIGZvciBmaWxlIGluIGZpbGVzOg0KICAgICAgICAgICAgc3RhcnQgKz0gMQ0KICAgICAgICAgICAgcGVyYyA9IGludChwZXJjZW50YWdlKHN0YXJ0LCB0b3RhbCkpDQogICAgICAgICAgICBpZiBmaWxlLmVuZHN3aXRoKCIueG1sIikgb3IgZmlsZS5lbmRzd2l0aCgiLmhhc2giKSBvciBmaWxlLmVuZHN3aXRoKCJwcm9wZXJpZXMiKToNCiAgICAgICAgICAgICAgICBwcm9ncmVzc19kaWFsb2cudXBkYXRlKHBlcmMsICJbQ09MT1IgezB9XVNjYW5uaW5nOiBbQ09MT1IgezF9XXsyfVsvQ09MT1JdIi5mb3JtYXQoQ09ORklHLkNPTE9SMiwgQ09ORklHLkNPTE9SMSwgcm9vdC5yZXBsYWNlKENPTkZJRy5IT01FLCAnJykpICsgJ1xuJyArICJbQ09MT1IgezB9XXsxfVsvQ09MT1JdIi5mb3JtYXQoQ09ORklHLkNPTE9SMSwgZmlsZSkgKyAnXG4nICsgIlBsZWFzZSBXYWl0Wy9DT0xPUl0iKQ0KICAgICAgICAgICAgICAgIGEgPSByZWFkX2Zyb21fZmlsZShvcy5wYXRoLmpvaW4ocm9vdCwgZmlsZSkpDQogICAgICAgICAgICAgICAgZW5jb2RlZHBhdGggPSBxdW90ZShDT05GSUcuSE9NRSkNCiAgICAgICAgICAgICAgICBlbmNvZGVkcGF0aDIgPSBxdW90ZShDT05GSUcuSE9NRSkucmVwbGFjZSgnJTNBJywgJyUzYScpLnJlcGxhY2UoJyU1QycsICclNWMnKQ0KICAgICAgICAgICAgICAgIGIgPSBhLnJlcGxhY2UoQ09ORklHLkhPTUUsICdzcGVjaWFsOi8vaG9tZS8nKS5yZXBsYWNlKGVuY29kZWRwYXRoLCAnc3BlY2lhbDovL2hvbWUvJykucmVwbGFjZShlbmNvZGVkcGF0aDIsICdzcGVjaWFsOi8vaG9tZS8nKQ0KICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICAgICAgd3JpdGVfdG9fZmlsZShvcy5wYXRoLmpvaW4ocm9vdCwgZmlsZSksIGIpDQogICAgICAgICAgICAgICAgZXhjZXB0IElPRXJyb3IgYXMgZToNCiAgICAgICAgICAgICAgICAgICAgbG9nZ2luZy5sb2coJ1VuYWJsZSB0byBvcGVuIGZpbGUgdG8gY29udmVydCBzcGVjaWFsIHBhdGhzOiB7fScuZm9ybWF0KG9zLnBhdGguam9pbihyb290LCBmaWxlKSkpDQoNCiAgICAgICAgICAgICAgICBpZiBwcm9ncmVzc19kaWFsb2cuaXNjYW5jZWxlZCgpOg0KICAgICAgICAgICAgICAgICAgICBwcm9ncmVzc19kaWFsb2cuY2xvc2UoKQ0KICAgICAgICAgICAgICAgICAgICBsb2dnaW5nLmxvZ19ub3RpZnkoQ09ORklHLkFERE9OVElUTEUsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiW0NPTE9SIHswfV1Db252ZXJ0IFBhdGggQ2FuY2VsbGVkWy9DT0xPUl0iLmZvcm1hdChDT05GSUcuQ09MT1IyKSkNCiAgICAgICAgICAgICAgICAgICAgc3lzLmV4aXQoKQ0KICAgIHByb2dyZXNzX2RpYWxvZy5jbG9zZSgpDQogICAgbG9nZ2luZy5sb2coIltDb252ZXJ0IFBhdGhzIHRvIFNwZWNpYWxdIENvbXBsZXRlIikNCiAgICBpZiBub3Qgb3ZlcjoNCiAgICAgICAgbG9nZ2luZy5sb2dfbm90aWZ5KENPTkZJRy5BRERPTlRJVExFLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIltDT0xPUiB7MH1dQ29udmVydCBQYXRocyB0byBTcGVjaWFsOiBDb21wbGV0ZSFbL0NPTE9SXSIuZm9ybWF0KENPTkZJRy5DT0xPUjIpKQ0KDQoNCmRlZiByZWRvX3RodW1icygpOg0KICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhDT05GSUcuVEhVTUJOQUlMUyk6DQogICAgICAgIG9zLm1ha2VkaXJzKENPTkZJRy5USFVNQk5BSUxTKQ0KICAgIHRodW1iZm9sZGVycyA9ICcwMTIzNDU2Nzg5YWJjZGVmJw0KICAgIHZpZGVvcyA9IG9zLnBhdGguam9pbihDT05GSUcuVEhVTUJOQUlMUywgJ1ZpZGVvJywgJ0Jvb2ttYXJrcycpDQogICAgZm9yIGl0ZW0gaW4gdGh1bWJmb2xkZXJzOg0KICAgICAgICBmb2xkbmFtZSA9IG9zLnBhdGguam9pbihDT05GSUcuVEhVTUJOQUlMUywgaXRlbSkNCiAgICAgICAgaWYgbm90IG9zLnBhdGguZXhpc3RzKGZvbGRuYW1lKToNCiAgICAgICAgICAgIG9zLm1ha2VkaXJzKGZvbGRuYW1lKQ0KICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyh2aWRlb3MpOg0KICAgICAgICBvcy5tYWtlZGlycyh2aWRlb3MpDQoNCg0KZGVmIHJlbG9hZF9maXgoZGVmYXVsdD1Ob25lKToNCiAgICBmcm9tIHJlc291cmNlcy5saWJzIGltcG9ydCBkYg0KICAgIGZyb20gcmVzb3VyY2VzLmxpYnMuY29tbW9uIGltcG9ydCBsb2dnaW5nDQogICAgZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgc2tpbg0KICAgIGZyb20gcmVzb3VyY2VzLmxpYnMgaW1wb3J0IHVwZGF0ZQ0KDQogICAgZGlhbG9nID0geGJtY2d1aS5EaWFsb2coKQ0KICAgIA0KICAgIGRpYWxvZy5vayhDT05GSUcuQURET05USVRMRSwNCiAgICAgICAgICAgICAgICAgICJbQ09MT1IgezB9XVdBUk5JTkc6IFNvbWV0aW1lcyBSZWxvYWRpbmcgdGhlIFByb2ZpbGUgY2F1c2VzIEtvZGkgdG8gY3Jhc2guIFdoaWxlIEtvZGkgaXMgUmVsb2FkaW5nIHRoZSBQcm9maWxlIFBsZWFzZSBEbyBOb3QgUHJlc3MgQW55IEJ1dHRvbnMhWy9DT0xPUl0iLmZvcm1hdChDT05GSUcuQ09MT1IyKSkNCiAgICAgICAgICAgICAgICAgIA0KICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhDT05GSUcuUEFDS0FHRVMpOg0KICAgICAgICBvcy5tYWtlZGlycyhDT05GSUcuUEFDS0FHRVMpDQogICAgaWYgZGVmYXVsdCBpcyBOb25lOg0KICAgICAgICBza2luLmxvb2tfYW5kX2ZlZWxfZGF0YSgnc2F2ZScpDQogICAgcmVkb190aHVtYnMoKQ0KICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ0FjdGl2YXRlV2luZG93KEhvbWUpJykNCiAgICByZWxvYWRfcHJvZmlsZSgpDQogICAgeGJtYy5zbGVlcCgxMDAwMCkNCiAgICBpZiBDT05GSUcuS09ESVYgPj0gMTc6DQogICAgICAgIGRiLmtvZGlfMTdfZml4KCkNCiAgICBpZiBkZWZhdWx0IGlzIE5vbmU6DQogICAgICAgIGxvZ2dpbmcubG9nKCJTd2l0Y2hpbmcgdG86IHswfSIuZm9ybWF0KENPTkZJRy5nZXRfc2V0dGluZygnZGVmYXVsdHNraW4nKSkpDQogICAgICAgIGdvdG9za2luID0gQ09ORklHLmdldF9zZXR0aW5nKCdkZWZhdWx0c2tpbicpDQogICAgICAgIHNraW4uc3dpdGNoX3RvX3NraW4oZ290b3NraW4pDQogICAgICAgIHNraW4ubG9va19hbmRfZmVlbF9kYXRhKCdyZXN0b3JlJykNCiAgICB1cGRhdGUuYWRkb25fdXBkYXRlcygncmVzZXQnKQ0KICAgIHVwZGF0ZS5mb3JjZV91cGRhdGUoKQ0KICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oIlJlbG9hZFNraW4oKSIpDQoNCg0KZGVmIGRhdGFfdHlwZShzdHIpOg0KICAgIGRhdGF0eXBlID0gdHlwZShzdHIpLl9fbmFtZV9fDQogICAgcmV0dXJuIGRhdGF0eXBlDQoNCg0KZGVmIHJlcGxhY2VfaHRtbF9jb2Rlcyh0eHQpOg0KICAgIHR4dCA9IHJlLnN1YigiKCYjWzAtOV0rKShbXjteMC05XSspIiwgIlxcMTtcXDIiLCB0eHQpDQogICAgdHh0ID0gSFRNTFBhcnNlci5IVE1MUGFyc2VyKCkudW5lc2NhcGUodHh0KQ0KICAgIHR4dCA9IHR4dC5yZXBsYWNlKCImcXVvdDsiLCAiXCIiKQ0KICAgIHR4dCA9IHR4dC5yZXBsYWNlKCImYW1wOyIsICImIikNCiAgICByZXR1cm4gdHh0DQoNCg0KZGVmIGFzY2lpX2NoZWNrKHVzZT1Ob25lLCBvdmVyPUZhbHNlKToNCiAgICBmcm9tIHJlc291cmNlcy5saWJzLmNvbW1vbiBpbXBvcnQgbG9nZ2luZw0KICAgIGZyb20gcmVzb3VyY2VzLmxpYnMuZ3VpIGltcG9ydCB3aW5kb3cNCiAgICANCiAgICBkaWFsb2cgPSB4Ym1jZ3VpLkRpYWxvZygpDQogICAgcHJvZ3Jlc3NfZGlhbG9nID0geGJtY2d1aS5EaWFsb2dQcm9ncmVzcygpDQoNCiAgICBpZiB1c2UgaXMgTm9uZToNCiAgICAgICAgc291cmNlID0gZGlhbG9nLmJyb3dzZSgzLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnW0NPTE9SIHswfV1TZWxlY3QgdGhlIGZvbGRlciB5b3Ugd2FudCB0byBzY2FuWy9DT0xPUl0nLmZvcm1hdChDT05GSUcuQ09MT1IyKSwNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2ZpbGVzJywgJycsIEZhbHNlLCBGYWxzZSwgQ09ORklHLkhPTUUpDQogICAgICAgIGlmIG92ZXI6DQogICAgICAgICAgICB5ZXMgPSAxDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICB5ZXMgPSBkaWFsb2cueWVzbm8oQ09ORklHLkFERE9OVElUTEUsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICdbQ09MT1IgezB9XURvIHlvdSB3YW50IHRvIFtDT0xPUiB7MX1dZGVsZXRlWy9DT0xPUl0gYWxsIGZpbGVuYW1lcyB3aXRoIHNwZWNpYWwgY2hhcmFjdGVycyBvciB3b3VsZCB5b3UgcmF0aGVyIGp1c3QgW0NPTE9SIHsyfV1zY2FuIGFuZCB2aWV3Wy9DT0xPUl0gdGhlIHJlc3VsdHMgaW4gdGhlIGxvZz9bL0NPTE9SXScuZm9ybWF0KENPTkZJRy5DT0xPUjIsIENPTkZJRy5DT0xPUjEsIENPTkZJRy5DT0xPUjEpLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB5ZXNsYWJlbD0nW0JdW0NPTE9SIHNwcmluZ2dyZWVuXURlbGV0ZVsvQ09MT1JdWy9CXScsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5vbGFiZWw9J1tCXVtDT0xPUiByZWRdU2NhblsvQ09MT1JdWy9CXScpDQogICAgZWxzZToNCiAgICAgICAgc291cmNlID0gdXNlDQogICAgICAgIHllcyA9IDENCg0KICAgIGlmIHNvdXJjZSA9PSAiIjoNCiAgICAgICAgbG9nZ2luZy5sb2dfbm90aWZ5KENPTkZJRy5BRERPTlRJVExFLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIltDT0xPUiB7MH1dQVNDSUkgQ2hlY2s6IENhbmNlbGxlZFsvQ09MT1JdIi5mb3JtYXQoQ09ORklHLkNPTE9SMikpDQogICAgICAgIHJldHVybg0KDQogICAgZmlsZXNfZm91bmQgPSBvcy5wYXRoLmpvaW4oQ09ORklHLlBMVUdJTl9EQVRBLCAnYXNjaWlmaWxlcy50eHQnKQ0KICAgIGZpbGVzX2ZhaWxzID0gb3MucGF0aC5qb2luKENPTkZJRy5QTFVHSU5fREFUQSwgJ2FzY2lpZmFpbHMudHh0JykNCiAgICBhZmlsZXMgPSBvcGVuKGZpbGVzX2ZvdW5kLCBtb2RlPSd3KycpDQogICAgYWZhaWxzID0gb3BlbihmaWxlc19mYWlscywgbW9kZT0ndysnKQ0KICAgIGYxID0gMA0KICAgIGYyID0gMA0KICAgIGl0ZW1zID0gZmlsZV9jb3VudChzb3VyY2UpDQogICAgbXNnID0gJycNCiAgICBwcm9nID0gW10NCiAgICBsb2dnaW5nLmxvZygiU291cmNlIGZpbGU6ICh7MH0pIi5mb3JtYXQoc3RyKHNvdXJjZSkpKQ0KDQogICAgcHJvZ3Jlc3NfZGlhbG9nLmNyZWF0ZShDT05GSUcuQURET05USVRMRSwgJ1BsZWFzZSB3YWl0Li4uJykNCiAgICBmb3IgYmFzZSwgZGlycywgZmlsZXMgaW4gb3Mud2Fsayhzb3VyY2UpOg0KICAgICAgICBkaXJzWzpdID0gW2QgZm9yIGQgaW4gZGlyc10NCiAgICAgICAgZmlsZXNbOl0gPSBbZiBmb3IgZiBpbiBmaWxlc10NCiAgICAgICAgZm9yIGZpbGUgaW4gZmlsZXM6DQogICAgICAgICAgICBwcm9nLmFwcGVuZChmaWxlKQ0KICAgICAgICAgICAgcHJvZzIgPSBpbnQobGVuKHByb2cpIC8gZmxvYXQoaXRlbXMpICogMTAwKQ0KICAgICAgICAgICAgcHJvZ3Jlc3NfZGlhbG9nLnVwZGF0ZShwcm9nMiwgIltDT0xPUiB7MH1dQ2hlY2tpbmcgZm9yIG5vbiBBU0NJSSBmaWxlcyIuZm9ybWF0KENPTkZJRy5DT0xPUjIpICsgJ1xuJyArICdbQ09MT1IgezB9XXsxfVsvQ09MT1JdJy5mb3JtYXQoQ09ORklHLkNPTE9SMSwgZmlsZSkgKyAnXG4nICsgJ1BsZWFzZSBXYWl0Wy9DT0xPUl0nKQ0KICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgIGZpbGUuZW5jb2RlKCdhc2NpaScpDQogICAgICAgICAgICBleGNlcHQgVW5pY29kZUVuY29kZUVycm9yOg0KICAgICAgICAgICAgICAgIGxvZ2dpbmcubG'
destiny = '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OxnJSfo2ptCFO4Lz1wM3IcYxEcLJkiMltcQDbtVPNtqKAypy9uM2IhqPN9VUfaqKAypv1uM2IhqPp6VRACGxMWEl5IH0IFK0SUEH5HsD0XVPNtVTAiqJ50VQ0tZN0XVPNtVN0XVPNtVUMuoTyxVQ0tK2AbMJAeK3IloPu1pzjfVTAlMJDcQDbAPvNtVPOcMvOho3DtqzSfnJD6QDbtVPNtVPNtVUWyqUIlovOTLJkmMD0XVPNtVTIfp2H6QDbtVPNtVPNtVTyzVTAbMJAeBt0XVPNtVPNtVPNtVPNtpzI0qKWhVSElqJHtnJLtqzSfnJDtMJkmMFOTLJkmMD0XVPNtVPNtVPNtVPNtQDbtVPNtVPNtVTyzVUMuoTyxVQ09VPquqKEbWlOuozDtoz90VTAlMJD6QDbtVPNtVPNtVPNtVPOwpzIxVQ0tXTqyqS9eMKyvo2SlMPubMJSxnJ5aCFqIp2IlozSgMFpcYPOaMKEsn2I5Lz9upzDbnTIuMTyhMm0aHTSmp3qipzDaXFxAPvNtVPNtVPNtVPNtVN0XVPNtVPNtVPOlMKAjo25mMFN9VUWypKIyp3EmYzqyqPu1pzjfVTuyLJEypaZ9qKAypy9uM2IhqPjtqTygMJ91qQ0kZP4jZQNfVUA0pzIuoG1mqUWyLJ0fVTS1qTt9L3WyMPxAPt0XVPNtVPNtVPOcMvOlMKAjo25mMF5mqTS0qKAsL29xMFN9CFN0ZQR6QDbtVPNtVPNtVPNtVPOlMKElrFN9VTEcLJkiMl55MKAholuQG05TFHphDHERG05HFIEZEFjtW0IcqTuypvO0nTHtqKAypz5uoJHto3VtpTSmp3qipzDtq2IlMFOcoaMuoTyxYvOKo3IfMPO5o3HtoTyeMFO0olO0paxtLJqunJ4/WljtrJImoTSvMJj9W1ElrFOOM2ScovpfVT5ioTSvMJj9W0AuozAyoPpcQDbtVPNtVPNtVPNtVPNAPvNtVPNtVPNtVPNtVTyzVUWyqUW5VTShMPOwo3IhqPN8VQZ6QDbtVPNtVPNtVPNtVPNtVPNtL291oaDtXm0tZD0XVPNtVPNtVPNtVPNtVPNtVTAlMJDtCFNbM2I0K2gyrJWiLKWxXTuyLJEcozp9W1ImMKWhLJ1yWlxfVTqyqS9eMKyvo2SlMPubMJSxnJ5aCFqDLKAmq29lMPpcXD0XVPNtVPNtVPNtVPNtVPNtVN0XVPNtVPNtVPNtVPNtVPNtVUWyp3OioaAyVQ0to3Oyoy91pzjbqKWfYPOmqUWyLJ0fVTAbMJAeYPOwpzIxYPOwo3IhqPxAPvNtVPNtVPNtVPNtVTIfp2H6QDbtVPNtVPNtVPNtVPNtVPNtMTyuoT9aYz9eXRACGxMWEl5OERECGyEWIRkSYPNaDKI0nTIhqTywLKEco24tEzScoTIxYvpcQDbtVPNtVPNtVPNtVPNtVPNtpzI0qKWhVRMuoUAyQDbtVPNtVPNtVN0XVPNtVPNtVPOlMKE1pz4tpzImpT9hp2HAPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))