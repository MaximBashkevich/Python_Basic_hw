def hist_text(string):
    orig_hist = dict()
    revert_hist = dict()
    for sym in string:
        if sym in orig_hist:
            orig_hist[sym] += 1
        else:
            orig_hist[sym] = 1
    print('Оригинальный словарь частот:')
    for i_sym in sorted(orig_hist.keys()):
        print(i_sym, ':', orig_hist[i_sym])

    for i_dict in orig_hist:
        lst = []
        if orig_hist[i_dict] in revert_hist:
            revert_hist[orig_hist[i_dict]].append(i_dict)
            # temp.append(i_dict)
            # revert_hist[orig_hist[i_dict]] = temp

        else:
            lst.append(i_dict)
            #qq = orig_hist[i_dict]
            revert_hist[orig_hist[i_dict]] = lst
    print('\nИнвертированный словарь частот:'
          )
    for i_count in sorted(revert_hist.keys()):
        print(i_count, ':', revert_hist[i_count])




text = input('Введите текст: ')
hist = hist_text(text)

