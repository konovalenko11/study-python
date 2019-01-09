
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']

m_list = []

for it1 in d:
    print("  L1: {}".format(it1))
    if not isinstance(it1, list):
        if 'm' in it1:
            m_list.append(it1)
        continue
    for it2 in it1:
        print("    L2: {}".format(it2))
        if not isinstance(it2, list):
            if 'm' in it2:
                m_list.append(it2)
            continue
        for it3 in it2:
            print("      L3: {}".format(it3))
            if not isinstance(it3, list):
                if 'm' in it3:
                    m_list.append(it3)
                continue