choose_area = None #0翻页，1行数，2盘面，3元素，4文件操作

# 需要变量来分别记录盘面和元素区域的点选情况
choose_board_grid = [None, None]
choose_ele_grid = [None, None]
grid_ele = {
    "[0,2]": 51,
    "[1,2]": 52,
}

choose_ele = None

lp_path = './levelProperty.xml'
lc_path = './levelsCleanUp.xml'
levelId = 0
maxLine = 9
startLine = 0

kv_map = {
    '51': {'id': '51', 'layer': '1', 'objectType': '1', 'picType': '0'},
    '52': {'id': '52', 'layer': '1', 'objectType': '1', 'picType': '1'},
}
