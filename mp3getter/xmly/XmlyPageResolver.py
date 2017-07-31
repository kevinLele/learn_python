# coding:utf-8

from mp3getter.utils.BaseUtils import log
import mp3getter.utils.WebUtils as WebUtils
import mp3getter.utils.FileUtils as FileUtils
import mp3getter.utils.DBUtils as DBUtils
import json
from bs4 import BeautifulSoup

'''
喜玛拉雅网页的解析器
'''

index = 1


# 通过传入的页面分析是否是分页的
#     1）如果是分页的则返回所有分页的访问地址
#     2）如果没有则直接返回主页面
def get_paging_from_main(url):
    main_html = WebUtils.get_page_html(url)
    soup = BeautifulSoup(main_html.text, "lxml")
    paging_bar_div = soup.find('div', {'class': 'pagingBar_wrapper'})

    paging_list = []

    # 检查是否有分页标签栏
    if paging_bar_div is not None:
        paging_buttons = paging_bar_div.findAll('a')

        for btn in paging_buttons:
            if btn.text.encode("utf-8").isdigit():
                paging_url = url + "?page=" + btn.text
                paging_list.append(paging_url)
    else:
        paging_list.append(url)

    return paging_list


# 解析页面并返回抓取的音频信息
def resolver_page(page_url):
    global index
    log('Page Url: ' + page_url)

    audio_list = []
    page_html = WebUtils.get_page_html(page_url)
    sound_list_div = BeautifulSoup(page_html.text, "lxml").findAll(attrs={'class': 'album_soundlist'})
    sound_list = sound_list_div[0].ul.findAll('li')

    for soundLi in sound_list:
        sound_id = soundLi.attrs['sound_id']
        sound_name = soundLi.find('a', {'class': 'title'}).attrs['title']

        json_url = 'http://www.ximalaya.com/tracks/' + sound_id + '.json'
        log('json_url: ' + json_url)
        json_html = WebUtils.get_page_html(json_url)
        log('json_html: ' + json_html.text)
        json_result = json.loads(json_html.text)
        sound_path = json_result['play_path']
        expanded_name = FileUtils.get_expanded_name(sound_path)

        print 'Audio Info : %d %s %s %s %s' % (index, sound_id, sound_name, expanded_name, sound_path)
        audio_list.append((sound_id, sound_name, expanded_name, sound_path))
        index += 1

    return audio_list


def get_audio_list(urls):
    audio_list = []

    for url in urls:
        audio_list.extend(resolver_page(url))

    return audio_list


def save_audio_list_to_db(audio_list):
    try:
        DBUtils.init_connection("audio.db")

        for idx, audio in enumerate(audio_list):
            # print '%d %s %s %s %s' % (idx + 1, audio[0], audio[1], audio[2], audio[3],)
            DBUtils.execute_sql("insert into audio (sn,id,name,extended,path) values (?,?,?,?,?)",
                                (idx + 1, audio[0], audio[1], audio[2], audio[3]))
        DBUtils.commit()
    finally:
        DBUtils.close_connection()


if __name__ == "__main__":
    # main_url = 'http://www.ximalaya.com/3999963/album/235740'
    # print get_page_from_paging(main_url)
    save_audio_list_to_db(
        get_audio_list(
            get_paging_from_main('http://www.ximalaya.com/29553933/album/2811947')))
    pass
