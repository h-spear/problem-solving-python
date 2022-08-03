# https://school.programmers.co.kr/learn/courses/30/lessons/42893

from collections import defaultdict
import re


def solution(word, pages):
    def get_default_score(page):
        page = re.sub(def_pattern, "0", page)
        fragments = page.split(word)
        score = 0
        for i in range(len(fragments) - 1):
            if not fragments[i] or not fragments[i + 1]:
                continue
            if fragments[i][-1].isalpha():
                continue
            if fragments[i + 1][0].isalpha():
                continue
            score += 1
        return score

    def save_infos(i, page):
        fragments = page.split('"')
        for frag in fragments:
            if len(frag) < 5:
                continue
            if frag[:5] == "(url)":
                map_url_to_idx[frag[5:]] = i
                map_idx_to_url[i] = frag[5:]
            if frag[:5] == "(ref)":
                map_idx_to_refc[i] += 1
                refs[frag[5:]].append(i)

    lp = len(pages)
    word = word.lower()

    default_score = [0] * lp
    ref_count = [0] * lp
    matching_score = [0] * lp

    refs = defaultdict(list)
    map_url_to_idx = dict()
    map_idx_to_url = dict()
    map_idx_to_refc = defaultdict(int)

    url_pattern = '<meta property="og:url" content="'
    ref_pattern = '<a href="'
    def_pattern = "[\\,\t,\n,\r]"

    # info setting
    for i in range(lp):
        pages[i] = pages[i].lower()
        pages[i] = re.sub(url_pattern, '"(url)', pages[i])
        pages[i] = re.sub(ref_pattern, '"(ref)', pages[i])
        save_infos(i, pages[i])
        default_score[i] = get_default_score(pages[i])

    # calc matching score
    for i in range(lp):
        url = map_idx_to_url[i]
        refs_idx = refs[url]
        link_score = 0
        for idx in refs_idx:
            if map_idx_to_refc[idx] == 0:
                continue
            link_score += default_score[idx] / map_idx_to_refc[idx]

        matching_score[i] = link_score + default_score[i]

    answer = 0
    maxx = -1
    for i, x in enumerate(matching_score):
        if x > maxx:
            answer = i
            maxx = x

    return answer
