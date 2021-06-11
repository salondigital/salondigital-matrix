import base64, codecs
magic = 'aW1wb3J0IHhibWMNCmltcG9ydCB4Ym1jYWRkb24NCmltcG9ydCB4Ym1jZ3VpDQppbXBvcnQgeGJtY3BsdWdpbg0KaW1wb3J0IHVybGxpYi5yZXF1ZXN0DQppbXBvcnQgcmUNCg0KaW1wb3J0IHN5cw0KaWYgc3lzLnZlcnNpb25faW5mb1swXSA+PSAzOg0KICAgIHVuaWNvZGUgPSBzdHINCg0KSU5TVEFMTF9QQUdFICAgICA9ICdodHRwOi8vc2Fsb25kaWdpdGFsLmVzL2NoZWNrLnBocCcNClVTRVJfQUdFTlQgICAJID0gJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdPVzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNDcuMC4yNTI2LjczIFNhZmFyaS81MzcuMzYgUmVwbGljYW50V2l6YXJkLzEuMC4wJw0KTUVNQkVSU19VUkwgICAgICA9ICdodHRwOi8vc2Fsb25kaWdpdGFsLmVzLycNCldJWkFSRF9QQUdFICAgICAgPSAnd2l6YXJkLnBocCcNCldJWkFSREZJTEUgICAgICAgPSAnaHR0cHM6Ly9zYWxvbmRpZ2l0YWwuZXMvd2l6YXJkLnBocCcNCkFERE9OVElUTEUgPSAnW0NPTE9SIHJlZF1bQl1TYWxvbkRpZ2l0YWxbL0JdWy9DT0xPUl0gQ29udHJvbCcNCg0KdHJ5OiAgIyBQeXRob24gMw0KICAgIGZyb20gdXJsbGliLnBhcnNlIGltcG9ydCBwYXJzZV9xc2wNCmV4Y2VwdCBJbXBvcnRFcnJvcjogICMgUHl0aG9uIDINCiAgICBmcm9tIHVybHBhcnNlIGltcG9ydCBwYXJzZV9xc2wNCg0KZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24uY29uZmlnIGltcG9ydCBDT05GSUcNCmZyb20gcmVzb3VyY2VzLmxpYnMuY29tbW9uIGltcG9ydCBsb2dnaW5nDQpmcm9tIHJlc291cmNlcy5saWJzLmNvbW1vbiBpbXBvcnQgdG9vbHMNCmZyb20gcmVzb3VyY2VzLmxpYnMuZ3VpIGltcG9ydCBtZW51DQpmcm9tIHJlc291cmNlcy5saWJzIGltcG9ydCB3aXphcmQgYXMgd2l6DQpmcm9tIHVybGxpYi5yZXF1ZXN0IGltcG9ydCB1cmxvcGVuDQoNCmFkdmFuY2VkX3NldHRpbmdzX21vZGUgPSAnYWR2YW5jZWRfc2V0dGluZ3MnDQphZGRvbl9pbnN0YWxsZXJfbW9kZSA9ICdhZGRvbnMnDQpESUFMT0cgICAgICAgICA9IHhibWNndWkuRGlhbG9nKCkNCmRlZiBnZXRTKG5hbWUpOg0KICAgICAgIHRyeTogcmV0dXJuIEFERE9OLmdldFNldHRpbmcobmFtZSkNCiAgICAgICBleGNlcHQ6IHJldHVybiBGYWxzZQ0KDQpkZWYgc2V0UyhuYW1lLCB2YWx1ZSk6DQogICAgICAgdHJ5OiBBRERPTi5zZXRTZXR0aW5nKG5hbWUsIHZhbHVlKQ0KICAgICAgIGV4Y2VwdDogcmV0dXJuIEZhbHNlDQoNCmRlZiBvcGVuUyhuYW1lPSIiKToNCiAgICAgICBBRERPTi5vcGVuU2V0dGluZ3MoKQ0KICAgICAgIA0KZGVmIGdldF9rZXlib2FyZChkZWZhdWx0PSIiLCBoZWFkaW5nPSIiLCBoaWRkZW49RmFsc2UpOg0KICAgIGtleWJvYXJkID0geGJtYy5LZXlib2FyZChkZWZhdWx0LCBoZWFkaW5nLCBoaWRkZW4pDQogICAga2V5Ym9hcmQuZG9Nb2RhbCgpDQogICAgaWYga2V5Ym9hcmQuaXNDb25maXJtZWQoKToNCiAgICAgICAgcmV0dXJuIGtleWJvYXJkLmdldFRleHQoKQ0KICAgIHJldHVybiBkZWZhdWx0DQogICAgDQpkZWYgc3VtaW5zdGFsbChyZWRvPUZhbHNlKToNCglpZiB3aXouZ2V0UygnbG9naW4nKSA9PSAnJyBvciB3aXouZ2V0UygncGFzcycpID09ICcnIG9yIHJlZG8gPT0gVHJ1ZToNCgkJaWYgcmVkbyA9PSBUcnVlOiBjaG9pY2UgPSAxDQoJCWVsc2U6IGNob2ljZSA9IERJQUxPRy55ZXNubyhBRERPTlRJVExFLCAiTmVjZXNpdGFzIGVzdGFyIHJlZ2lzdHJhZG8gcGFyYSBhY2NlZGVyIGEgbGFzIGFjdHVhbGl6YWNpb25lcyBkZSAlcyEiICUgQURET05USVRMRSwgIlF1aWVyZXMgaW50cm9kdWNpciB0dXMgZGF0b3MgZGUgdXN1YXJpbz8iLCAiUG9yIGZhdm9yLCByZWdpc3RyYXRlIGVuIGVsIGZvcm8gZGUgJXMgcGFyYSBhY2NlZGVyISIgJSBNRU1CRVJTX1VSTCwgeWVzbGFiZWw9IkludHJvZHVjaXIgZGF0b3MiLCBub2xhYmVsPSJDYW5jZWxhciIpDQoJCWlmIGNob2ljZSA9PSAxOiANCgkJCWxvZ2luICAgID0gZ2V0X2tleWJvYXJkKGhlYWRpbmc9J0ludHJvZHVjZSB0dSBFTUFJTCB1c2FkbyBwYXJhIGVsIHJlZ2lzdHJvIGVuIGVsIGZvcm8gZGUgU0QnKQ0KCQkJcGFzc3dvcmQgPSBnZXRfa2V5Ym9hcmQoaGVhZGluZz0nSW50cm9kdWNlIHR1IFBhc3N3b3JkJykNCgkJCXhibWNhZGRvbi5BZGRvbigncGx1Z2luLnByb2dyYW0uaGlkZGVuc2QtbWluaS1tYXRyaXgnKS5zZXRTZXR0aW5nKCdsb2dpbicsIGxvZ2luKQ0KCQkJeGJtY2FkZG9uLkFkZG9uKCdwbHVnaW4ucHJvZ3JhbS5oaWRkZW5zZC1taW5pLW1hdHJpeCcpLnNldFNldHRpbmcoJ3Bhc3MnLCBwYXNzd29yZCkNCgkJZWxzZToNCgkJCXN5cy5leGl0KCkNCgl1cmwgPSBJTlNUQUxMX1BBR0UgKyAiP2VtYWlsPSIgKyB4Ym1jYWRkb24uQWRkb24oJ3BsdWdpbi5wcm9ncmFtLmhpZGRlbnNkLW1pbmktbWF0cml4JykuZ2V0U2V0dGluZygnbG9naW4nKSArICImcGFzcz0iICsgeGJtY2FkZG9uLkFkZG9uKCdwbHVnaW4ucHJvZ3JhbS5oaWRkZW5zZC1taW5pLW1hdHJpeCcpLmdldFNldHRpbmcoJ3Bhc3MnKQ0KCWxpbmsgID0gd2l6Lm9wZW5VUkwodXJsKS5yZXBsYWNlKCdcbicsICcnKS5yZXBsYWNlKCdccicsICcnKQ0KCXRvdGFsID0gcmUuY29tcGlsZSgnaW5zdGFsbD0iKFxkKSInKS5maW5kYWxsKGxpbmspDQoJdHJ5Og0KCQlpZiAobGluayAhPSAnMScpOg0KCQkJc3lzLmV4aXQoKQ0KCWV4Y2VwdDogDQoJCWlmIERJQUxPRy55ZXNubygnRXJyb3IgZGUgYXV0ZW50aWZpY2FjaW9uJywgJ1BvciBmYXZvciwgcmVnaXN0cmF0ZSBlbiBlbCBmb3JvIGRlIGNsaWVudGVzJywgeWVzbGFiZWw9IkludHJvZHVjaXIgZGF0b3MiLCBub2xhYmVsPSJDYW5jZWxhciIpOg0KCQkJc3VtaW5zdGFsbChUcnVlKQ0KCQllbHNlOg0KCQkJc3lzLmV4aXQoKQ0KICAgICAgICAgICAgICANCmNsYXNzIFJvdXRlcjoNCiAgICBkZWYgX19pbml0X18oc2VsZik6DQogICAgICAgIHNlbGYucm91dGUgPSBOb25lDQogICAgICAgIHNlbGYucGFyYW1zID0ge30NCiAgICAgICAgdG9vbHMuZW5zdXJlX2ZvbGRlcnMoKQ0KDQogICAgZGVmIF9sb2dfcGFyYW1zKHNlbGYsIHBhcmFtc3RyaW5nKToNCiAgICAgICAgX3VybCA9IHN5cy5hcmd2WzBdDQoNCiAgICAgICAgc2VsZi5wYXJhbXMgPSBkaWN0KHBhcnNlX3FzbChwYXJhbXN0cmluZykpDQoNCiAgICAgICAgbG9nc3RyaW5nID0gJ3swfTogJy5mb3JtYXQoX3VybCkNCiAgICAgICAgZm9yIHBhcmFtIGluIHNlbGYucGFyYW1zOg0KICAgICAgICAgICAgbG9nc3RyaW5nICs9ICdbIHswfTogezF9IF0gJy5mb3JtYXQocGFyYW0sIHNlbGYucGFyYW1zW3BhcmFtXSkNCg0KICAgICAgICBsb2dnaW5nLmxvZyhsb2dzdHJpbmcsIGxldmVsPXhibWMuTE9HREVCVUcpDQoNCiAgICAgICAgcmV0dXJuIHNlbGYucGFyYW1zDQoNCiAgICBkZWYgZGlzcGF0Y2goc2VsZiwgaGFuZGxlLCBwYXJhbXN0cmluZyk6DQogICAgICAgIHNlbGYuX2xvZ19wYXJhbXMocGFyYW1zdHJpbmcpDQoNCiAgICAgICAgbW9kZSA9IHNlbGYucGFyYW1zWydtb2RlJ10gaWYgJ21vZGUnIGluIHNlbGYucGFyYW1zIGVsc2UgTm9uZQ0KICAgICAgICB1cmwgPSBzZWxmLnBhcmFtc1sndXJsJ10gaWYgJ3VybCcgaW4gc2VsZi5wYXJhbXMgZWxzZSBOb25lDQogICAgICAgIG5hbWUgPSBzZWxmLnBhcmFtc1snbmFtZSddIGlmICduYW1lJyBpbiBzZWxmLnBhcmFtcyBlbHNlIE5vbmUNCiAgICAgICAgYWN0aW9uID0gc2VsZi5wYXJhbXNbJ2FjdGlvbiddIGlmICdhY3Rpb24nIGluIHNlbGYucGFyYW1zIGVsc2UgTm9uZQ0KDQogICAgICAgICMgTUFJTiBNRU5VDQogICAgICAgIGlmIG1vZGUgaXMgTm9uZToNCiAgICAgICAgICAgIGZyb20gcmVzb3VyY2VzLmxpYnMuZ3VpLm1haW5fbWVudSBpbXBvcnQgTWFpbk1lbnUNCiAgICAgICAgICAgIE1haW5NZW51KCkuZ2V0X2xpc3RpbmcoKQ0KICAgICAgICAgICAgc2VsZi5fZmluaXNoKGhhbmRsZSkNCg0KICAgICAgICAjIFNFVFRJTkdTDQogICAgICAgIGVsaWYgbW9kZSA9PSAnc2V0dGluZ3MnOiAgIyBPcGVuV2l6YXJkIHNldHRpbmdzDQogICAgICAgICAgICBDT05GSUcub3Blbl9zZXR0aW5ncyhuYW1lKQ0KICAgICAgICAgICAgeGJtYy5leGVjdXRlYnVpbHRpbignQ29udGFpbmVyLlJlZnJlc2goKScpDQogICAgICAgIGVsaWYgbW9kZSA9PSAnb3BlbnNldHRpbmdzJzogICMgT3BlbiBvdGhlciBhZGRvbnMnIHNldHRpbmdzDQogICAgICAgICAgICBzZXR0aW5nc19pZCA9IGV2YWwodXJsLnVwcGVyKCkgKyAnSUQnKVtuYW1lXVsncGx1Z2luJ10NCiAgICAgICAgICAgIENPTkZJRy5vcGVuX3NldHRpbmdzKHNldHRpbmdzX2lkKQ0KICAgICAgICAgICAgeGJtYy5leGVjdXRlYnVpbHRpbignQ29udGFpbmVyLlJlZnJlc2goKScpDQogICAgICAgIGVsaWYgbW9kZSA9PSAndG9nZ2xlc2V0dGluZyc6ICAjIFRvZ2dsZSBhIHNldHRpbmcNCiAgICAgICAgICAgIENPTkZJRy5zZXRfc2V0dGluZyhuYW1lLCAnZmFsc2UnIGlmIENPTkZJRy5nZXRfc2V0dGluZyhuYW1lKSA9PSAndHJ1ZScgZWxzZSAndHJ1ZScpDQogICAgICAgICAgICB4Ym1jLmV4ZWN1dGVidWlsdGluKCdDb250YWluZXIuUmVmcmVzaCgpJykNCg0KICAgICAgICAjIE1FTlUgU0VDVElPTlMNCiAgICAgICAgZWxpZiBtb2RlID09ICdidWlsZHMnOiAgIyBCdWlsZHMNCiAgICAgICAgICAgIHN1bWluc3RhbGwoKQ0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicy5ndWkuYnVpbGRfbWVudSBpbXBvcnQgQnVpbGRNZW51DQogICAgICAgICAgICBCdWlsZE1lbnUoKS5nZXRfbGlzdGluZygpDQogICAgICAgICAgICBzZWxmLl9maW5pc2goaGFuZGxlKQ0KICAgICAgICBlbGlmIG1vZGUgPT0gJ3ZpZXdidWlsZCc6ICAjIEJ1aWxkcyAtPiAiWW91ciBCdWlsZCINCiAgICAgICAgICAgIGZyb20gcmVzb3VyY2VzLmxpYnMuZ3VpLmJ1aWxkX21lbnUgaW1wb3J0IEJ1aWxkTWVudQ0KICAgICAgICAgICAgQnVpbGRNZW51KCkudmlld19idWlsZChuYW1lKQ0KICAgICAgICAgICAgc2VsZi5fZmluaXNoKGhhbmRsZSkNCiAgICAgICAgZWxpZiBtb2RlID09ICdidWlsZGluZm8nOiAgIyBCdWlsZHMgLT4gQnVpbGQgSW5mbw0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicy5ndWkuYnVpbGRfbWVudSBpbXBvcnQgQnVpbGRNZW51DQogICAgICAgICAgICBCdWlsZE1lbnUoKS5idWlsZF9pbmZvKG5hbWUpDQogICAgICAgIGVsaWYgbW9kZSA9PSAnYnVpbGRwcmV2aWV3JzogICMgQnVpbGRzIC0+IEJ1aWxkIFByZXZpZXcNCiAgICAgICAgICAgIGZyb20gcmVzb3VyY2VzLmxpYnMuZ3VpLmJ1aWxkX21lbnUgaW1wb3J0IEJ1aWxkTWVudQ0KICAgICAgICAgICAgQnVpbGRNZW51KCkuYnVpbGRfdmlkZW8obmFtZSkNCiAgICAgICAgZWxpZiBtb2RlID09ICdpbnN0YWxsJzogICMgQnVpbGRzIC0+IEZyZXNoIEluc3RhbGwvU3RhbmRhcmQgSW5zdGFsbC9BcHBseSBndWlmaXgNCiAgICAgICAgICAgIGZyb20gcmVzb3VyY2VzLmxpYnMud2l6YXJkIGltcG9ydCBXaXphcmQNCg0KICAgICAgICAgICAgaWYgYWN0aW9uID09ICdidWlsZCc6DQogICAgICAgICAgICAgICAgV2l6YXJkKCkuYnVpbGQobmFtZSkNCiAgICAgICAgICAgIGVsaWYgYWN0aW9uID09ICdndWknOg0KICAgICAgICAgICAgICAgIFdpemFyZCgpLmd1aShuYW1lKQ0KICAgICAgICAgICAgZWxpZiBhY3Rpb24gPT0gJ3RoZW1lJzogICMgQnVpbGRzIC0+ICJZb3VyIEJ1aWxkIiAtPiAiWW91ciBUaGVtZSINCiAgICAgICAgICAgICAgICBXaXphcmQoKS50aGVtZShuYW1lLCB1cmwpDQoNCiAgICAgICAgZWxpZiBtb2RlID09ICdtYWludCc6ICAjIE1haW50ZW5hbmNlICsgTWFpbnRlbmFuY2UgLT4gYW55ICJUb29scyIgc2VjdGlvbg0KICAgICAgICAgICAgc3VtaW5zdGFsbCgpDQogICAgICAgICAgICBmcm9tIHJlc291cmNlcy5saWJzLmd1aS5tYWludGVuYW5jZV9tZW51IGltcG9ydCBNYWludGVuYW5jZU1lbnUNCg0KICAgICAgICAgICAgaWYgbmFtZSA9PSAnY2xlYW4nOg0KICAgICAgICAgICAgICAgIE1haW50ZW5hbmNlTWVudSgpLmNsZWFuX21lbnUoKQ0KICAgICAgICAgICAgZWxpZiBuYW1lID09ICdhZGRvbic6DQogICAgICAgICAgICAgICAgTWFpbnRlbmFuY2VNZW51KCkuYWRkb25fbWVudSgpDQogICAgICAgICAgICBlbGlmIG5hbWUgPT0gJ21pc2MnOg0KICAgICAgICAgICAgICAgIE1haW50ZW5hbmNlTWVudSgpLm1pc2NfbWVudSgpDQogICAgICAgICAgICBlbGlmIG5hbWUgPT0gJ2JhY2t1cCc6DQogICAgICAgICAgICAgICAgTWFpbnRlbmFuY2VNZW51KCkuYmFja3VwX21lbnUoKQ0KICAgICAgICAgICAgZWxpZiBuYW1lID09ICd0d2Vha3MnOg0KICAgICAgIC'
love = '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'
god = 'ICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ0NvbnRhaW5lci5SZWZyZXNoKCknKQ0KICAgICAgICBlbGlmIG1vZGUgPT0gJ3doaXRlbGlzdCc6ICAjIFdoaXRlbGlzdCBGdW5jdGlvbnMNCiAgICAgICAgICAgIGZyb20gcmVzb3VyY2VzLmxpYnMgaW1wb3J0IHdoaXRlbGlzdA0KICAgICAgICAgICAgd2hpdGVsaXN0LndoaXRlbGlzdChuYW1lKQ0KDQogICAgICAgICMgIENMRUFOSU5HDQogICAgICAgIGVsaWYgbW9kZSA9PSAnb2xkVGh1bWJzJzogICMgQ2xlYW5pbmcgVG9vbHMgLT4gQ2xlYXIgT2xkIFRodW1ibmFpbHMNCiAgICAgICAgICAgIGZyb20gcmVzb3VyY2VzLmxpYnMgaW1wb3J0IGNsZWFyDQogICAgICAgICAgICBjbGVhci5vbGRfdGh1bWJzKCkNCiAgICAgICAgZWxpZiBtb2RlID09ICdjbGVhcmJhY2t1cCc6ICAjIEJhY2t1cC9SZXN0b3JlIC0+IENsZWFuIFVwIEJhY2sgVXAgRm9sZGVyDQogICAgICAgICAgICBmcm9tIHJlc291cmNlcy5saWJzIGltcG9ydCBiYWNrdXANCiAgICAgICAgICAgIGJhY2t1cC5jbGVhbnVwX2JhY2t1cCgpDQogICAgICAgIGVsaWYgbW9kZSA9PSAnZnVsbGNsZWFuJzogICMgQ2xlYW5pbmcgVG9vbHMgLT4gVG90YWwgQ2xlYW51cA0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgY2xlYXINCiAgICAgICAgICAgIGNsZWFyLnRvdGFsX2NsZWFuKCkNCiAgICAgICAgICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ0NvbnRhaW5lci5SZWZyZXNoKCknKQ0KICAgICAgICBlbGlmIG1vZGUgPT0gJ2NsZWFyY2FjaGUnOiAgIyBDbGVhbmluZyBUb29scyAtPiBDbGVhciBDYWNoZQ0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgY2xlYXINCiAgICAgICAgICAgIGNsZWFyLmNsZWFyX2NhY2hlKCkNCiAgICAgICAgICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ0NvbnRhaW5lci5SZWZyZXNoKCknKQ0KICAgICAgICBlbGlmIG1vZGUgPT0gJ2NsZWFyZnVuY3Rpb25jYWNoZSc6ICAjIENsZWFuaW5nIFRvb2xzIC0+IENsZWFyIEZ1bmN0aW9uIENhY2hlcw0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgY2xlYXINCiAgICAgICAgICAgIGNsZWFyLmNsZWFyX2Z1bmN0aW9uX2NhY2hlKCkNCiAgICAgICAgICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ0NvbnRhaW5lci5SZWZyZXNoKCknKQ0KICAgICAgICBlbGlmIG1vZGUgPT0gJ2NsZWFycGFja2FnZXMnOiAgIyBDbGVhbmluZyBUb29scyAtPiBDbGVhciBQYWNrYWdlcw0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgY2xlYXINCiAgICAgICAgICAgIGNsZWFyLmNsZWFyX3BhY2thZ2VzKCkNCiAgICAgICAgICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ0NvbnRhaW5lci5SZWZyZXNoKCknKQ0KICAgICAgICBlbGlmIG1vZGUgPT0gJ2NsZWFyY3Jhc2gnOiAgIyBDbGVhbmluZyBUb29scyAtPiBDbGVhciBDcmFzaCBMb2dzDQogICAgICAgICAgICBmcm9tIHJlc291cmNlcy5saWJzIGltcG9ydCBjbGVhcg0KICAgICAgICAgICAgY2xlYXIuY2xlYXJfY3Jhc2goKQ0KICAgICAgICAgICAgeGJtYy5leGVjdXRlYnVpbHRpbignQ29udGFpbmVyLlJlZnJlc2goKScpDQogICAgICAgIGVsaWYgbW9kZSA9PSAnY2xlYXJ0aHVtYic6ICAjIENsZWFuaW5nIFRvb2xzIC0+IENsZWFyIFRodW1ibmFpbHMNCiAgICAgICAgICAgIGZyb20gcmVzb3VyY2VzLmxpYnMgaW1wb3J0IGNsZWFyDQogICAgICAgICAgICBjbGVhci5jbGVhcl90aHVtYnMoKQ0KICAgICAgICAgICAgeGJtYy5leGVjdXRlYnVpbHRpbignQ29udGFpbmVyLlJlZnJlc2goKScpDQogICAgICAgIGVsaWYgbW9kZSA9PSAnY2xlYXJhcmNoaXZlJzogICMgQ2xlYW5pbmcgVG9vbHMgLT4gQ2xlYXIgQXJjaGl2ZSBDYWNoZQ0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgY2xlYXINCiAgICAgICAgICAgIGNsZWFyLmNsZWFyX2FyY2hpdmUoKQ0KICAgICAgICAgICAgeGJtYy5leGVjdXRlYnVpbHRpbignQ29udGFpbmVyLlJlZnJlc2goKScpDQogICAgICAgIGVsaWYgbW9kZSA9PSAnZnJlc2hzdGFydCc6ICAjIENsZWFuaW5nIFRvb2xzIC0+IEZyZXNoIFN0YXJ0DQogICAgICAgICAgICBmcm9tIHJlc291cmNlcy5saWJzIGltcG9ydCBpbnN0YWxsDQogICAgICAgICAgICBpbnN0YWxsLmZyZXNoX3N0YXJ0KCkNCiAgICAgICAgZWxpZiBtb2RlID09ICdwdXJnZWRiJzogICMgQ2xlYW5pbmcgVG9vbHMgLT4gUHVyZ2UgRGF0YWJhc2VzDQogICAgICAgICAgICBmcm9tIHJlc291cmNlcy5saWJzIGltcG9ydCBkYg0KICAgICAgICAgICAgZGIucHVyZ2VfZGIoKQ0KICAgICAgICBlbGlmIG1vZGUgPT0gJ3JlbW92ZWFkZG9ucyc6ICAjIEFkZG9uIFRvb2xzIC0+IFJlbW92ZSBBZGRvbnMNCiAgICAgICAgICAgIGZyb20gcmVzb3VyY2VzLmxpYnMgaW1wb3J0IGNsZWFyDQogICAgICAgICAgICBjbGVhci5yZW1vdmVfYWRkb25fbWVudSgpDQogICAgICAgIGVsaWYgbW9kZSA9PSAncmVtb3ZlZGF0YSc6ICAjIEFkZG9uIFRvb2xzIC0+IFJlbW92ZSBBZGRvbiBEYXRhDQogICAgICAgICAgICBmcm9tIHJlc291cmNlcy5saWJzIGltcG9ydCBjbGVhcg0KICAgICAgICAgICAgY2xlYXIucmVtb3ZlX2FkZG9uX2RhdGEobmFtZSkNCiAgICAgICAgZWxpZiBtb2RlID09ICdyZXNldGFkZG9uJzogICMgQWRkb24gVG9vbHMgLT4gUmVtb3ZlIEFkZG9uIERhdGEgLT4gUmVtb3ZlICBXaXphcmQgQWRkb24gRGF0YQ0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24gaW1wb3J0IHRvb2xzDQoNCiAgICAgICAgICAgIHRvb2xzLmNsZWFuX2hvdXNlKENPTkZJRy5BRERPTl9EQVRBLCBpZ25vcmU9VHJ1ZSkNCiAgICAgICAgICAgIGxvZ2dpbmcubG9nX25vdGlmeSgiW0NPTE9SIHswfV17MX1bL0NPTE9SXSIuZm9ybWF0KENPTkZJRy5DT0xPUjEsIENPTkZJRy5BRERPTlRJVExFKSwNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiW0NPTE9SIHswfV1BZGRvbl9EYXRhIHJlc2V0Wy9DT0xPUl0iLmZvcm1hdChDT05GSUcuQ09MT1IyKSkNCiAgICAgICAgIyBCQUNLVVAgLyBSRVNUT1JFDQogICAgICAgIGVsaWYgbW9kZSA9PSAnYmFja3VwJyBhbmQgYWN0aW9uOg0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgYmFja3VwDQogICAgICAgICAgICBiYWNrdXAuYmFja3VwKGFjdGlvbikNCiAgICAgICAgZWxpZiBtb2RlID09ICdyZXN0b3JlJyBhbmQgYWN0aW9uOg0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgcmVzdG9yZQ0KICAgICAgICAgICAgcmVzdG9yZS5yZXN0b3JlKGFjdGlvbiwgZXh0ZXJuYWw9bmFtZSA9PSAnZXh0ZXJuYWwnKQ0KDQogICAgICAgIGVsaWYgbW9kZSA9PSAnd2l6YXJkdXBkYXRlJzogICMgV2l6YXJkIFVwZGF0ZQ0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgdXBkYXRlDQogICAgICAgICAgICB1cGRhdGUud2l6YXJkX3VwZGF0ZSgpDQoNCiAgICAgICAgIyBMT0dHSU5HDQogICAgICAgIGVsaWYgbW9kZSA9PSAndXBsb2FkbG9nJzogICMgVXBsb2FkIExvZyBGaWxlDQogICAgICAgICAgICBzdW1pbnN0YWxsKCkNCiAgICAgICAgICAgIGxvZ2dpbmcudXBsb2FkX2xvZygpDQogICAgICAgIGVsaWYgbW9kZSA9PSAndmlld2xvZyc6ICAjIFZpZXcga29kaS5sb2cNCiAgICAgICAgICAgIHN1bWluc3RhbGwoKQ0KICAgICAgICAgICAgbG9nZ2luZy52aWV3X2xvZ19maWxlKCkNCiAgICAgICAgZWxpZiBtb2RlID09ICd2aWV3d2l6bG9nJzogICMgVmlldyB3aXphcmQubG9nDQogICAgICAgICAgICBzdW1pbnN0YWxsKCkNCiAgICAgICAgICAgIGZyb20gcmVzb3VyY2VzLmxpYnMuZ3VpIGltcG9ydCB3aW5kb3cNCiAgICAgICAgICAgIHdpbmRvdy5zaG93X2xvZ192aWV3ZXIobG9nX2ZpbGU9Q09ORklHLldJWkxPRykNCiAgICAgICAgZWxpZiBtb2RlID09ICd2aWV3ZXJyb3Jsb2cnOiAgIyBWaWV3IGVycm9ycyBpbiBsb2cNCiAgICAgICAgICAgIHN1bWluc3RhbGwoKQ0KICAgICAgICAgICAgbG9nZ2luZy5lcnJvcl9jaGVja2luZygpDQogICAgICAgIGVsaWYgbW9kZSA9PSAndmlld2Vycm9ybGFzdCc6ICAjIFZpZXcgbGFzdCBlcnJvciBpbiBsb2cNCiAgICAgICAgICAgIHN1bWluc3RhbGwoKQ0KICAgICAgICAgICAgbG9nZ2luZy5lcnJvcl9jaGVja2luZyhsYXN0PVRydWUpDQogICAgICAgIGVsaWYgbW9kZSA9PSAnY2xlYXJ3aXpsb2cnOiAgIyBDbGVhciB3aXphcmQubG9nDQogICAgICAgICAgICBmcm9tIHJlc291cmNlcy5saWJzLmNvbW1vbiBpbXBvcnQgdG9vbHMNCiAgICAgICAgICAgIHRvb2xzLnJlbW92ZV9maWxlKENPTkZJRy5XSVpMT0cpDQogICAgICAgICAgICBsb2dnaW5nLmxvZ19ub3RpZnkoIltDT0xPUiB7MH1dezF9Wy9DT0xPUl0iLmZvcm1hdChDT05GSUcuQ09MT1IxLCBDT05GSUcuQURET05USVRMRSksDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIltDT0xPUiB7MH1dV2l6YXJkIExvZyBDbGVhcmVkIVsvQ09MT1JdIi5mb3JtYXQoQ09ORklHLkNPTE9SMikpDQoNCiAgICAgICAgIyBBRFZBTkNFRCBTRVRUSU5HUw0KICAgICAgICBlbGlmIG1vZGUgPT0gYWR2YW5jZWRfc2V0dGluZ3NfbW9kZToNCiAgICAgICAgICAgIGZyb20gcmVzb3VyY2VzLmxpYnMgaW1wb3J0IGFkdmFuY2VkDQoNCiAgICAgICAgICAgIHNlbGYucm91dGUgPSBhZHZhbmNlZC5BZHZhbmNlZE1lbnUoKQ0KICAgICAgICAgICAgYWR2YW5jZWRfc2V0dGluZ3NfYWN0aW9ucyA9IFsncXVpY2tfY29uZmlndXJlJywgJ3ZpZXdfY3VycmVudCcsICdyZW1vdmVfY3VycmVudCcsICd3cml0ZV9hZHZhbmNlZCcsICdzZXRfc2V0dGluZycsICdzaG93X3NlY3Rpb24nXQ0KDQogICAgICAgICAgICBjYXRlZ29yeSA9IHNlbGYucGFyYW1zWydjYXRlZ29yeSddIGlmICdjYXRlZ29yeScgaW4gc2VsZi5wYXJhbXMgZWxzZSBOb25lDQogICAgICAgICAgICB0YWcgPSBzZWxmLnBhcmFtc1sndGFnJ10gaWYgJ3RhZycgaW4gc2VsZi5wYXJhbXMgZWxzZSBOb25lDQogICAgICAgICAgICB2YWx1ZSA9IHNlbGYucGFyYW1zWyd2YWx1ZSddIGlmICd2YWx1ZScgaW4gc2VsZi5wYXJhbXMgZWxzZSBOb25lDQogICAgICAgICAgICB0YWdzID0gc2VsZi5wYXJhbXNbJ3RhZ3MnXSBpZiAndGFncycgaW4gc2VsZi5wYXJhbXMgZWxzZSBOb25lDQoNCiAgICAgICAgICAgIGlmIG5vdCBhY3Rpb246DQogICAgICAgICAgICAgICAgc2VsZi5yb3V0ZS5zaG93X21lbnUodXJsPXVybCkNCiAgICAgICAgICAgICAgICBzZWxmLl9maW5pc2goaGFuZGxlKQ0KICAgICAgICAgICAgZWxpZiBhY3Rpb24gPT0gYWR2YW5jZWRfc2V0dGluZ3NfYWN0aW9uc1swXTogICMgQWR2YW5jZWQgU2V0dGluZ3MgUXVpY2sgQ29uZmlndXJlDQogICAgICAgICAgICAgICAgc2VsZi5yb3V0ZS5xdWlja19jb25maWd1cmUoKQ0KICAgICAgICAgICAgICAgIHNlbGYuX2ZpbmlzaChoYW5kbGUpDQogICAgICAgICAgICBlbGlmIGFjdGlvbiA9PSBhZHZhbmNlZF9zZXR0aW5nc19hY3Rpb25zWzFdOiAgIyBWaWV3IEN1cnJlbnQgQWR2YW5jZWQgU2V0dGluZ3MNCiAgICAgICAgICAgICAgICBhZHZhbmNlZC52aWV3X2N1cnJlbnQoKQ0KICAgICAgICAgICAgZWxpZiBhY3Rpb24gPT0gYWR2YW5jZWRfc2V0dGluZ3NfYWN0aW9uc1syXTogICMgUmVtb3ZlIEN1cnJlbnQgQWR2YW5jZWQgU2V0dGluZ3MNCiAgICAgICAgICAgICAgICBhZHZhbmNlZC5yZW1vdmVfY3VycmVudCgpDQogICAgICAgICAgICBlbGlmIGFjdGlvbiA9PSBhZHZhbmNlZF9zZXR0aW5nc19hY3Rpb25zWzNdIGFuZCB1cmw6ICAjIFdyaXRlIE5ldyBBZHZhbmNlZCBTZXR0aW5ncw0KICAgICAgICAgICAgICAgIHNlbGYucm91dGUud3JpdGVfYWR2YW5jZWQobmFtZSwgdXJsKQ0KICAgICAgICAgICAgZWxpZiBhY3Rpb24gPT0gYWR2YW5jZWRfc2V0dGluZ3NfYWN0aW9uc1s0XTogICMgU2V0IGEgU2V0dGluZw0KICAgICAgICAgICAgICAgIHNlbGYucm91dGUuc2V0X3NldHRpbmcoY2F0ZWdvcnksIHRhZywgdmFsdWUpDQogICAgICAgICAgICBlbGlmIGFjdGlvbiA9PSBhZHZhbmNlZF9zZXR0aW5nc19hY3Rpb25zWzVdOiAgIyBPcGVuIGEgU2VjdGlvbg0KICAgICAgICAgICAgICAgIHNlbGYucm91dGUuc2hvd19zZWN0aW9uKHRhZ3MpDQogICAgICAgICAgICAgICAgc2VsZi5fZmluaXNoKGhhbmRsZSkNCiAgICAgICAgICAgICAgICANCiAgICAgICAgIyBBRERPTiBJTlNUQUxMRVINCiAgICAgICAgZWxpZiBtb2RlID09IGFkZG9uX2luc3RhbGxlcl9tb2RlOg0KICAgICAgICAgICAgZnJvbSByZXNvdXJjZXMubGlicy5ndWkgaW1wb3J0IGFkZG9uX21lbnUNCi'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))