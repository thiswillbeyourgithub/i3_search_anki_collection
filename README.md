# i3_search_anki_database
python script and i3 binding to quickly browse your anki collection


Here's my i3 binding:
`bindsym $mod+b exec i3-input -F "exec /path_to/python3 /path_to/i3_seach_anki_collection/__init__.py --query='%s'" -l 50 -P "Search anki: "`
