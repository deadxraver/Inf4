with open('schedule.xml', encoding='utf-8') as f:
    with open('schedule.rtf', 'w', encoding='utf-8') as s:
        s.write(f.read())
