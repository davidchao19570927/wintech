# -*- coding: utf-8 -*-

from __main__ import *
global Opt2ActFrm,timezone,ChxStatus,GPIO,p4bee,Alert
#========================= get_var ===============================
def get_var():
    possibles = globals().copy()
    possibles.update(locals())
    return possibles
#=============================================================
#======================= def getSignInt(val) ==========================
def getSignInt(val):
    if val > 0x7FFFFFFF:
        x = val -0x100000000
    else:
        x = val
    return x
#=============================================================
#=============== class watchdog (threading.Thread) ==================
'''
class watchdog (threading.Thread):
    def __init__(self, threadID, name, event, stopper):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.event = event
        self.stopper = stopper
        self.IOVal = None
        self.chkCount = []
        self.isConti = True
        
    def run(self):
        global curPath,thisOS,StatusBar
        curPath = GetGlobals('curPath')
        thisOS = GetGlobals('thisOS')
        StatusBar = GetGlobals('StatusBar')
        self.img = curPath +'//watchdog.png'

        while self.stopper and not self.event.wait(10.0):
            if self.isConti:
                try:
                    StatusBar.ClockFrm.fig.savefig(self.img, dpi = 72)
                    if os.path.isfile(self.img):
                        with open(self.img, 'rb') as f:
                            _img = f.read()
                            _io = io.BytesIO(_img)
                            if _io.getvalue() != self.IOVal:
                                self.IOVal = _io.getvalue()
                                self.chkCount = []
                                #print('Status Good!')
                            else:
                                self.chkCount.append(time.time())
                                pass
                    else:
                        self.chkCount.append(time.time())
                        pass
                except:
                    self.chkCount.append(time.time())
                    pass
            else:
                self.chkCount = []

            if len(self.chkCount) == 0:
                #print('Status Good!')
                pass
            elif ((len(self.chkCount) >0) and (len(self.chkCount) <=12)):
                #if (len(self.chkCount) %3) == 0:
                    #print('HandOn times:', len(self.chkCount))
                pass
            else:     #約 120 sec 重啟
                if thisOS == 'Linux' :
                    p = subprocess.Popen('sudo shutdown -r now', stdout = subprocess.PIPE, shell = True)
                    pass
                elif thisOS == 'Windows' :
                    print('WatchDog auto reboot!')
                    self.chkCount = []
                    pass

            if not self.stopper:
                break
'''
#=============================================================
#=================== def runSubFrun(val) ============================
def runSubFrun(val):
    global subform,root,Opt2ActFrm,thread4combiTrig,stopFlag4combi,Alert
    global tilbar,VisualNumPad,container,BlandFrm,StatusBar,onoffswitch_var

    if type(root) == mainform:
        onoffswitch_var = GetGlobals('onoffswitch_var')
        StatusBar = GetGlobals('StatusBar')

            onoffswitch_var.set(val)

        if StatusBar.refreshIdlefun is not None:
            StatusBar.after_cancel(StatusBar.refreshIdlefun)
            StatusBar.refreshIdlefun = None
            #print(StatusBar.refreshIdlefun)
        
        root.isSuccessful = None
        BlandFrm = GetGlobals('BlandFrm')
        BlandFrm.tmpUnmap = time.time()
        BlandFrm.numUnmap = 0
        BlandFrm.after(100, BlandFrm.update_clock)
        BlandFrm.tkraise()
        #BlandFrm._job = BlandFrm.after(100, BlandFrm.update_clock)
        #container.place_forget()
        '''
        root.waitproc.set('Waiting ......')
        root.wait = waitmessage(None)

        if type(root.wait) != waitmessage:
            while type(root.wait) != waitmessage:
                time.sleep(0.05)
                if type(root.wait) == waitmessage:
                    root.wait.place(x = (root.winfo_width() -root.wait.winfo_reqwidth())/2,
                                    y = (root.winfo_height() -root.wait.winfo_reqheight())/2)
                    root.wait.tkraise()
                    break
        else:
            root.wait.place(x = (root.winfo_width() -root.wait.winfo_reqwidth())/2,
                            y = (root.winfo_height() -root.wait.winfo_reqheight())/2)
            root.wait.tkraise()
        '''
    thisFrm = tilBar.control_variable.get()
    thisFrm = [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if thisFrm in x][0])][0]

    if val == 1:    #啟動測試
        try:
            thread4combiTrig
        except:
            '''
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            '''
            thread4combiTrig = []
            #stopFlag4combi = threading.Event()       #1s
            for i in GroupSet:
                #thread4combiTrig.append(subform.TransADConv(1, "thread4combiTrig", stopFlag4combi, True, i))
                #thread4combiTrig[-1].daemon = True
                thread4combiTrig.append(subform.TransADConv(1000 +i, "thread4combiTrig%s" %i, True, i))
                thread4combiTrig[-1].start()
                while thread4combiTrig[-1].isSuccessful != val:
                    time.sleep(0.5)
                    pass
            #root.isSuccessful = val
            '''
            stopFlag4combi = threading.Event()       #1s
            thread4combiTrig = subform.TransADConv(1, "thread4combiTrig", stopFlag4combi, True)
            thread4combiTrig.daemon = True
            thread4combiTrig.start()
            '''
            pass
    else:   #暫停測試
        try:
            thread4combiTrig
            for _i in range(0, len(thread4combiTrig)):
                #print(_i, thread4combiTrig[_i])
                thread4combiTrig[_i].stopper = False
                thread4combiTrig[_i].join(1)
                _t0 = time.time()
                while thread4combiTrig[_i].isSuccessful != val:
                    if time.time() -_t0 >1.0:
                        print('thread4combiTrig[%s] error.' %_i)
                        break
                    time.sleep(0.5)
                    pass
            #root.isSuccessful = val
            '''
            #stopFlag4combi.set()
            thread4combiTrig.stopper = False
            thread4combiTrig.join()
            '''
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
    root.isSuccessful = val
    if thisFrm != '00001':

        if ((Alert.isTkraise == 0) and (onoffswitch_var.get() == 1)):
            tilBar.control_variable.set(Opt2ActFrm['00001'][0])
            ActivePage(tilBar.control_variable.get())

#=============================================================
#====== def showgroup(val) ====================================
def showgroup(val):
    global viewGP,StatusBar,maxch4grp,tilBar,GroupSet,AlarmCfg,Opt2ActFrm,Config4Lan
    #viewGP = val
    ##showgrouplnk == {0: [0, '1、2通道', [0, 1]], 1: [1, '3、4通道', [0, 1]], 2: [2, '5、6通道', [0, 1]]} or 
    ##{0: [0, '1通道', [0]], 1: [0, '2通道', [1]], 2: [1, '3通道', [0]], 3: [1, '4通道', [1]], 4: [2, '5通道', [0]], 5: [2, '6通道', [1]]}
    ##val == showgrouplnk.keys()[x]
    StatusBar = GetGlobals('StatusBar')
    viewGP = StatusBar.showgrouplnk[val][0]
    #print(viewGP, val)
    UpdateGlobals('viewGP', viewGP)
    tilBar = GetGlobals('tilBar')
    maxch4grp = GetGlobals('maxch4grp')
    GroupSet = GetGlobals('GroupSet')
    AlarmCfg = GetGlobals('AlarmCfg')
    Opt2ActFrm = GetGlobals('Opt2ActFrm')
    StatusBar.showgroup_var.set(StatusBar.showgrouplnk[val][1])
    #StatusBar.showgroup_var.set(StatusBar.showgrouplnk[viewGP])
    lKey = [key for key in Opt2ActFrm.keys() if 'TrendFrm' in Opt2ActFrm[key]][0]
    if len([x for x in Opt2ActFrm.values() if tilBar.control_variable.get() in x]) >0:
        #lKey = [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if tilBar.control_variable.get() in x][0])][0]
        lKey = [key for key in Opt2ActFrm.keys() if 'TrendFrm' in Opt2ActFrm[key]][0]

    for i in range(1, (maxch4grp +1)):
        #'tilBarFrm_til : LHGGDGNEOGNHJENHCGAFLHGGDG'
        _til = [(Config4Lan.get(AlarmCfg['lang'], 'LHGGDGNEOGNHJENHCGAFLHGGDG', vars={'para1': GroupSet[viewGP]['ch'][i -1]})),
                ('%s %s' %(Config4Lan.get(AlarmCfg['lang'], 'channel'), GroupSet[viewGP]['ch'][i -1]))]
        #_til = [(Config4Lan.get(AlarmCfg['lang'], 'LHGGDGNEOGNHJENHCGAFLHGGDG', vars={'para1': GroupSet[viewGP]['ch'][i -1]})),
                #('%s %s' %(Config4Lan.get(AlarmCfg['lang'], 'channel'), GroupSet[(StatusBar.showgrouplnk[val][0])]['ch'][i -1]))]

        vars(tilBar)[('Ch%sCalcf ' %i)].config(text = _til[0])
        if (i -1) in StatusBar.showgrouplnk[val][2]:
            vars(tilBar)[('Ch%sCalcf ' %i)].grid()
        else:
            vars(tilBar)[('Ch%sCalcf ' %i)].grid_remove() #不在list中的不顯示

        if lKey is not None:
            path4mv[i].set_visible(((i -1) in StatusBar.showgrouplnk[val][2]))
            path4trend[i].set_visible(((i -1) in StatusBar.showgrouplnk[val][2]))
            Opt2ActFrm[lKey][2].legend.get_texts()[i -1].set_text(_til[1])
            Opt2ActFrm[lKey][2].updateChart()
            
        prpd4main[i][0].set_visible(((i-1) in StatusBar.showgrouplnk[val][2]))
        otherfig['wave']['path'][i][0].set_visible(((i -1) in StatusBar.showgrouplnk[val][2]))
        otherfig['fft']['path'][i][0].set_visible(((i -1) in StatusBar.showgrouplnk[val][2]))
        otherfig['twmap']['path'][i][0].set_visible(((i -1) in StatusBar.showgrouplnk[val][2]))

        #vars(tilBar)[('Ch%sCalcf ' %i)].config(text = _til[0])
        #Opt2ActFrm[lKey][2].legend.get_texts()[i -1].set_text(_til[1])
#=============================================================
#=============================================================
def resetData(*args):
    global GroupSet, viewGP,curPath,path4phas,thread4UpdateCalcFrm
    global mmap_wave,resetTimes,onoffswitch_var,status,status,p4bee
    global FileLock,wait4reboot,thisOS,gainDict,trivitem,dbpath,loadconfig,Opt2ActFrm,trivitem
    print('resetData:', time.time(), *args)
    mmap_wave = GetGlobals('mmap_wave')
    resetTimes = GetGlobals('resetTimes')
    onoffswitch_var = GetGlobals('onoffswitch_var')
    StatusBar = GetGlobals('StatusBar')
    GroupSet = GetGlobals('GroupSet')
    AlarmCfg = GetGlobals('AlarmCfg')
    wait4reboot = GetGlobals('wait4reboot')
    thisOS = GetGlobals('thisOS')
    Opt2ActFrm = GetGlobals('Opt2ActFrm')
    gainDict = GetGlobals('gainDict')
    trivitem = GetGlobals('trivitem')
    _st = time.time()
    if 'thread4UpdateCalcFrm' not in globals():
        globals()['thread4UpdateCalcFrm'] = refreshGlobals()['thread4UpdateCalcFrm']
    gr = []
    if len(args) >0:
        if type(args) == tuple:
            #print(args) #([0, 1, 2],) ([0],) ([1],) ([2],)
            [gr.append(_grp) for _grp in args[0]]   #建立 reset 陣列
            _rst = []
            _chkdb = False

            dbpath = GetGlobals('dbpath')
            curPath = GetGlobals('curPath')
            db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
            db.execute("PRAGMA journal_mode=WAL")
            cursor  = db.cursor()
                        
            for _gr in gr:
                #GroupSet = GetGlobals('GroupSet')
                i = StatusBar.showgrouplnk[_gr][0]  #grp->gri
                #print('i:', i, all(len(GroupSet[i]['data4main'][j]['y']) == 0 for j in range(0, len(GroupSet[i]['ch']))))  #i: 0 True | i: 1 True | i: 2 True
                if (all(val == False for val in GroupSet[i]['autotrig'])):   #無法再調整TrigLv. & Gain
                    if i not in _rst:   # i in GroupSet[i]
                        _rst.append(i)
                        resetTimes.append([_st, int(i)])
                elif (all(val == None for val in GroupSet[i]['autotrig'])):
                    pass
                else:
                    #change triglv. gain
                    print('Gr : %s，Auto Change Trigger.[ch:%s, lev:%s, gain:%s]' %(i, GroupSet[i]['autotrig'][0], GroupSet[i]['autotrig'][1], GroupSet[i]['autotrig'][2]))
                    #=================================================
                    try:
                        _trigch = float(GroupSet[i]['autotrig'][0])
                        _chglev = float(GroupSet[i]['autotrig'][1])
                        _chgain = float(GroupSet[i]['autotrig'][2])
                        _chkda = True
                        _chkdb = True
                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                        _chkda = False

                    if _chkda:
                        GroupSet[i]['trig_ch'] =  GroupSet[i]['autotrig'][0]
                        GroupSet[i]['trig_lv'] = GroupSet[i]['autotrig'][1]
                        #print("gr:", i, "type(GroupSet[i]['trig_lv']:", type(GroupSet[i]['trig_lv']), GroupSet[i]['trig_lv'])
                        GroupSet[i]['gain'] = GroupSet[i]['autotrig'][2]

                        GroupSet[i]['cmdline'] = bytearray([
                            GroupSet[i]['trig_ch'],
                            int((GroupSet[i]['trig_lv'] +741.7) /7.6),
                            GroupSet[i]['wave_out'],
                            GroupSet[i]['fft_out'],
                            GroupSet[i]['prpd_out'],
                            GroupSet[i]['twmap_out'],
                            GroupSet[i]['sync_opt'],
                            GroupSet[i]['list_choose'],
                            GroupSet[i]['gain']
                            ])
                        cursor.execute('update adc_setting set trig_ch = ?, trig_lv = ?, gain = ? where sn = ?',
                                       [GroupSet[i]['autotrig'][0], GroupSet[i]['autotrig'][1], GroupSet[i]['autotrig'][2], i])

                        GroupSet[i]['cmdfp'].seek(0)
                        GroupSet[i]['cmdfp'].write(GroupSet[i]['cmdline'])
                        GroupSet[i]['autotrig'] = [None, None, None]

                        #==============================================================================
                        _gainary = [('00000000' +bin(GroupSet[i]['gain'])[2:])[-8:][:4],
                                    ('00000000' +bin(GroupSet[i]['gain'])[2:])[-8:][-4:]]
                        _i = 0
                        for _ii in GroupSet[i]['ch']:
                            try:
                                _gain = [key for key in gainDict if gainDict[key][_i] == _gainary[_i]][0]
                            except Exception as e:
                                exc_type, exc_obj, exc_tb = sys.exc_info()
                                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                                print(exc_type, fname, exc_tb.tb_lineno)
                                _gain = '10x'
                            vars(Opt2ActFrm['00005'][2])[('Ch%s_gain_variable' %_ii)].set(_gain)
                            vars(Opt2ActFrm['00005'][2])[('Gr%s_Conf' %i)].Grx_trigLv.set((list(trivitem.keys())[list(trivitem.values()).index(GroupSet[i]['trig_lv'])]))
                            _i = _i +1
                        #=================================================================================
            #=================================================
            if _chkdb:
                db.commit()
                cursor.execute("select * from alarmcfg")
                alarm_res = cursor.fetchone()
                adc_res = cursor.fetchall()
                cursor.close()
                db.close()
                global loadconfig
                loadconfig.getAlarmcfg(alarm_res)  #輸出參數
                UpdateGlobals('GroupSet', GroupSet)
                pass
            del _rst,_chkdb
        else:
            pass
    else:#reset 按鈕只清除可視群組
        _grp = [key for key in list(StatusBar.showgrouplnk.keys()) if StatusBar.showgrouplnk[key][1] == StatusBar.showgroup_var.get()][0]
        gr.append(_grp)
        del _grp
        #gr.append(viewGP)   #無指定群組，只清除可視群組(適PDD)
        #print('reset viewGP:', datetime.datetime.fromtimestamp(_st), 'Gr:', viewGP)
        #print(args) #()

    #======================================================
    FileLock = GetGlobals('FileLock')
    _t0 = time.time()
    while FileLock:
        time.sleep(0.5)
        FileLock = GetGlobals('FileLock')
        if ((not FileLock) or ((time.time() -_t0) > 2.0)):
            break
    del _t0

    if not FileLock:
        FileLock = True

        for _gr in gr:
        #for i in gr:
            i = StatusBar.showgrouplnk[_gr][0]  # i in GroupSet[i]
            mmap_k = list(GroupSet[i]['mmap'].keys())
            for _mi in range(0, len(mmap_k)):
                float_array = {
                    'durat': lambda: [0.0, 0.0, 0.0, _st, _st, 0.0, 0.0, 0.0, _st, _st, 0.0, 0.0, 0.0, _st, _st],
                    'prpd': lambda: array('f', [65535.0] *4),
                    'twmap': lambda: array('f', [65535.0] *4),
                    'wave': lambda: array('f', [0.0] *1024),
                    'fft': lambda: array('f', [0.0] *512)
                    }.get(mmap_k[_mi], lambda : array('f', [0.0] *1024))()

                if mmap_k[_mi] in ['wave', 'fft']:
                    for j in StatusBar.showgrouplnk[_gr][2]:
                        if mmap_k[_mi] == 'wave':
                            GroupSet[i]['mmap'][mmap_k[_mi]].seek((j *512 *4))
                            _temp = array('f', float_array[((j) *512) : (((j) *512) +512)])
                        else:
                            GroupSet[i]['mmap'][mmap_k[_mi]].seek((j *256 *4))
                            _temp = array('f', float_array[((j) *256) : (((j) *256) +256)])

                        _temp.tofile(GroupSet[i]['mmap'][mmap_k[_mi]])
                    #GroupSet[i]['mmap'][mmap_k[_mi]].seek(0)
                    #float_array.tofile(GroupSet[i]['mmap'][mmap_k[_mi]])
                elif mmap_k[_mi] == 'durat':
                    for j in StatusBar.showgrouplnk[_gr][2]: #[0, 1], [0], [1]
                        GroupSet[i]['mmap'][mmap_k[_mi]].seek(5 *(j) *8)
                        _temp = array('d', float_array[((j) *5) : (((j) *5) +5)])
                        _temp.tofile(GroupSet[i]['mmap'][mmap_k[_mi]])
                    '''    
                    GroupSet[i]['mmap'][mmap_k[_mi]].seek(0)
                    #GroupSet[i]['mmap'][mmap_k[_mi]].write(struct.pack('%sd' %len(float_array), *float_array))
                    #float_array.tofile(GroupSet[i]['mmap'][mmap_k[_mi]])
                    '''
                    '''
                    if _pdstatus != 3.0:
                        float_array.append(0.0)
                        #GroupSet[i]['mmap']['durat'].seek(-8, 2)
                        #GroupSet[i]['mmap']['durat'].write(struct.pack('d', 0.0))
                    float_array = array('d', float_array)
                    float_array.tofile(GroupSet[i]['mmap'][mmap_k[_mi]])
                    '''
                elif mmap_k[_mi] in ['prpd', 'twmap']:
                    try:
                        if AlarmCfg['chx_sel']: #單通道觸發
                            _temp = list(array('f', GroupSet[i]['mmap'][mmap_k[_mi]][:]))
                            nRec = len(_temp)    #筆數

                            for j in StatusBar.showgrouplnk[_gr][2]: #[0, 1], [0], [1]
                                for jj in range(2 *j, nRec, 4):
                                    GroupSet[i]['mmap'][mmap_k[_mi]][jj *4 : jj *4 +8] = array('f', [65535.0] *2)
                            del _temp, nRec
                            #print(list(array('f', GroupSet[i]['mmap'][mmap_k[_mi]][:])))

                        else:
                            GroupSet[i]['mmap'][mmap_k[_mi]].resize(len(float_array) *4)
                            GroupSet[i]['mmap'][mmap_k[_mi]].seek(0)
                            float_array.tofile(GroupSet[i]['mmap'][mmap_k[_mi]])
                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno, mmap_k[_mi], type(GroupSet[i]['mmap'][mmap_k[_mi]]), j, nRec)
                    '''
                    try:
                        GroupSet[i]['mmap'][mmap_k[_mi]].resize(len(float_array) *4)
                        GroupSet[i]['mmap'][mmap_k[_mi]].seek(0)
                        float_array.tofile(GroupSet[i]['mmap'][mmap_k[_mi]])
                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                    '''
            if _gr in list(thread4UpdateCalcFrm.oldstatus.keys()):
                thread4UpdateCalcFrm.oldstatus.pop(_gr)       #清除舊狀態
            #if i in list(thread4UpdateCalcFrm.oldstatus.keys()):
                #thread4UpdateCalcFrm.oldstatus.pop(i)       #清除舊狀態

            #======== 初始各記憶陣列 ============
            _pdstatus = array('d', GroupSet[i]['mmap']['durat'][:])[-1]
            _pdstatus = {True : lambda : hex(int(_pdstatus))[2:].zfill(2)[::-1],    #轉16進制併轉置
                         False : lambda : bin(int(_pdstatus))[2:].zfill(2)[::-1]
                         }.get(AlarmCfg['chx_sel'], lambda : bin(_pdstatus)[2:].zfill(2)[::-1])()
            _pdstatus = list(_pdstatus) #['0', '0'],['0', '1'],['1', '1'],['1', '0'] ||  ['0', '0'],['0', '1'],['0', '2'],['1', '0'],['1', '1'],['1', '2'],['2', '0'],['2', '1'],['2', '2']
            #print('_pdstatus:', _pdstatus)
            _pds = [_pdstatus[k] for k in StatusBar.showgrouplnk[_gr][2]]   #k = [0, 1], [0], [1]
            _pds = "".join(_pds)    #'00','01','10','11' || '0', '1', '2'
            #_pds = int(_pds)    #0, 1, 2, 3 || 0, 1, 2
            
            for j in StatusBar.showgrouplnk[_gr][2]:    #[0, 1], [0], [1]
                    GroupSet[i]['chxpds'][j] = 0.0
                    GroupSet[i]['chxdurat'][j] = 0.0
                    GroupSet[i]['inittime'][j] = _st
                    GroupSet[i]['lasttime'][j] = _st
                    GroupSet[i]['data4wave'][j] = {'x' :[], 'y': []}
                    GroupSet[i]['data4fft'][j] = {'x' :[], 'y': []}
                    GroupSet[i]['data4main'][j] = {'x' :[], 'y': []}
                    GroupSet[i]['data4twmp'][j] = {'x' :[], 'y': []}

                    if ((_pds == '11') or (_pds == '2')):
                        #print('_pds:', _pds)
                        pass
                    else:
                        #print('reset lighter:', _pds, type(_pds), 'j:', j)
                        _pdstatus[j] = '0'

            _pdss = ''.join(_pdstatus)
            _pdss = _pdss[::-1]
            _pdss = {True : lambda : float(int(_pdss, 16)),    #轉16進制
                     False : lambda : float(int(_pdss, 2))
                     }.get(AlarmCfg['chx_sel'], lambda : float(int(_pdss, 2)))()
            GroupSet[i].update({'oldalarstat': [_pdss, None]})
            GroupSet[i]['mmap']['durat'].seek(-8, 2)
            GroupSet[i]['mmap']['durat'].write(struct.pack('d', _pdss))
            
            '''
            GroupSet[i].update(
                {
                    'chxpds': [0.0 for j in range(0, len(GroupSet[i]['ch']) +1)],
                    'chxdurat': [0.0 for j in range(0, len(GroupSet[i]['ch']) +1)],
                    'inittime': [_st for j in range(0, len(GroupSet[i]['ch']) +1)],
                    'lasttime': [_st for j in range(0, len(GroupSet[i]['ch']) +1)],
                    #'oldalarstat': [0, None],
                    'mv':{0:{}, 1:{}},
                    'data4wave' : { 0: {'x' :[], 'y': []}, 1: {'x' :[], 'y': []}},
                    'data4fft' : { 0: {'x' :[], 'y': []}, 1: {'x' :[], 'y': []}},
                    'data4main' : { 0: {'x' :[], 'y': []}, 1: {'x' :[], 'y': []}},
                    'data4twmp' : { 0: {'x' :[], 'y': []}, 1: {'x' :[], 'y': []}}
                    })

            if GroupSet[i]['oldalarstat'][0] != 2:
                GroupSet[i].update({'oldalarstat': [0, None]})
            '''
                
        UpdateGlobals('GroupSet', GroupSet)
        FileLock = False
        UpdateGlobals('FileLock', FileLock)
        #print([GroupSet[x]['oldalarstat'] for x in GroupSet ])
    #======================================================
    #============= 清除燈號 ==============
    #print([(GroupSet[x]['oldalarstat'][0] +int(AlarmCfg['chx_sel'])) for x in GroupSet ])
    try:
        #=========================================
        #int(AlarmCfg['chx_sel']        0
        #int('11', 2)                           3 ===================> 3
        #=========================================
        #int(AlarmCfg['chx_sel']        1
        #int('22', 16)                      34 ===================> 35
        #int('21', 16)                      33 ===================> 34
        #int('20', 16)                      32 ===================> 33
        #int('02', 16)                      2 ===================> 3
        #int('12', 16)                      18 ===================> 19
        #=========================================
        #print([(GroupSet[x]['oldalarstat'][0] +int(AlarmCfg['chx_sel'])) for x in GroupSet ]
        alt_ary = [x for x in GroupSet if ((GroupSet[x]['oldalarstat'][0] +int(AlarmCfg['chx_sel'])) in [3, 19, 33, 34, 35])]
    except:
        alt_ary = []
    #print('alt_ary:', alt_ary)
    try:
        #=========================================
        #int(AlarmCfg['chx_sel']        0
        #int('01', 2)                           1 ===================> 1
        #int('10', 2)                           2 ===================> 2
        #=========================================
        #int(AlarmCfg['chx_sel']        1
        #int('01', 16)                      1 ===================> 2
        #int('10', 16)                      16 ===================> 17
        #int('11', 16)                      17 ===================> 18
        #=========================================
        #int('01', 2), int('10', 2), int('11', 16), int('01', 16), int('10', 16) +int(AlarmCfg['chx_sel']
        wry_ary = [x for x in GroupSet if ((GroupSet[x]['oldalarstat'][0] +int(AlarmCfg['chx_sel'])) in [1, 2, 17, 18])]
    except:
        wry_ary = []

    if len(alt_ary) == 0:   #無告警狀態群組，即復歸
        try:
            GPIO.output(AlarmCfg['bee_pin'], False)
        except:
            pass

        p4bee = GetGlobals('p4bee')
        if p4bee != None:
            try:
                p4bee.stopper = False
                p4bee.join()
                #del p4bee
                PopGlobals('p4bee')
            except:
                pass
    else:
        #print(alt_ary)
        pass


    #print(wry_ary)
    if len(wry_ary)  == 0:  #無告警狀態群組，即復歸
        try:
            GPIO.output(AlarmCfg['yl_pin'], False)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            pass
    else:   #代表仍有告警群組
        #print(wry_ary)
        pass
    #================================
    resetFunc(0)
    '''
    try:
        resetFunc(0)   #複歸reset狀態，寫入
    except:
        possibles = refreshGlobals()
        resetFunc = possibles.get('resetFunc')
        resetFunc(0)
    '''
    #====== 利用 on/off 重置 ==============
    if len(resetTimes) >= 10 :
        if (((resetTimes[-1][0] -resetTimes[0][0]) >=85) and
            ((resetTimes[-1][0] -resetTimes[0][0]) <= 105)):  #(10s *9) *1.1
            wait4reboot.append([_st])
            #print('wait4reboot size:', len(wait4reboot))
            #===== 關閉 serial port，與重啟 =====
            for i in GroupSet:
                try:
                    while GroupSet[i]['ser'].is_open:
                        GroupSet[i]['ser'].close()
                        time.sleep(0.5)
                except:
                    pass

            for i in GroupSet:
                try:
                    while not GroupSet[i]['ser'].is_open:
                        GroupSet[i]['ser'].open()
                        time.sleep(0.5)
                except:
                    pass
            print('reset serial', datetime.datetime.fromtimestamp(time.time()), 'wait4reboot size:', len(wait4reboot))
            #===========================
        else:
            wait4reboot = deque(maxlen = 10)
            UpdateGlobals('wait4reboot', wait4reboot)
        resetTimes = deque(maxlen = 10) #重計數
        UpdateGlobals('resetTimes', resetTimes)

    #=======================================
    if len(wait4reboot) >= 10:    #Reboot
        if AlarmCfg['demo'] != 98:
            if thisOS == 'Linux' :
                p = subprocess.Popen('sudo shutdown -r now', stdout = subprocess.PIPE, shell = True)
                pass
            elif thisOS == 'Windows' :
                wait4reboot = deque(maxlen = 10)
                UpdateGlobals('wait4reboot', wait4reboot)
                print('Computer will reboot!')
        else:
            wait4reboot = deque(maxlen = 10)
            UpdateGlobals('wait4reboot', wait4reboot)
            pass
    #========================================
    UpdateGlobals('resetTimes', resetTimes)
    UpdateGlobals('wait4reboot', wait4reboot)
    #================================
#========================= MainFrm2 =============================
class MainFrm2(tk.Frame):
    def __init__(self, parent, controller, law):
        global curPath,tilBar,StatusBar,figDpi
        global AlarmCfg,disp_var,viewGP
        global fig4main,showgroup_var,ax4main
        global path4phas,path4trig
        global chk_0_Img,chk_1_Img,Config4Lan
        global otherfig,prpd4main,maxch4grp

        tk.Frame.__init__(self,parent)
        h = parent['height'] -tilBar['height'] -StatusBar['height']
        self.config(relief = tk.GROOVE, bg = '#ffffff', width = parent['width'] -40, height = h)
        self.place(x = 0, y = tilBar['height'])
        self.law = law
        self.refreshtime = 0.0
        self.maxA = 0.0
        #self.data4wave = {1:{'x':[], 'y':[]}, 2:{'x':[], 'y':[]}}
        #self.data4fft = {1:{'x':[], 'y':[]}, 2:{'x':[], 'y':[]}}
        self.data4main = {}
        self.data4twmap = {}


        self.icon4resetDATA = tk.PhotoImage(file = (curPath +"//trash2.png"))
        resetDATABtn = tk.Button(self, text='', font = ('IPAGothic', 13, 'bold'),
                                 image = self.icon4resetDATA, compound="center",
                                 command = lambda val = 1 : resetFunc(val))
                                 #command = lambda val = 1 : self.resetFunc(val))
        resetDATABtn.place(x = (self.winfo_reqwidth() -resetDATABtn.winfo_reqwidth()),
                           y = (h -resetDATABtn.winfo_reqheight()))


        #================= 濾波器 ==========================
        '''
        self.isfilter_var = tk.IntVar()
        self.isfilter_var.set(0)
        self.isfilter = tk.Checkbutton(self, variable = self.isfilter_var,
                                       bd = 0, relief = tk.FLAT, image = chk_0_Img,
                                       selectimage = chk_1_Img, onvalue = 1,
                                       offvalue = 0,
                                       command = self.chkfilter)
        self.isfilter.config(activebackground = "#ffffff",bg = "#ffffff", indicatoron  = 0)
        self.isfilter.config(compound = tk.LEFT, state = tk.NORMAL)
        #'isfilter = GGMHJGGGDGLHKGNH'
        self.isfilter.config(text = Config4Lan.get(AlarmCfg['lang'], 'GGMHJGGGDGLHKGNH'),
                             font = ('IPAGothic', 13, 'bold'))
        ''''''
        self.isfilter.config(text = {
            'zh-TW' : lambda : '濾波',
            'en-US' : lambda : 'Filter',
            }.get(AlarmCfg['lang'], lambda : '濾波')(),
                             font = ('IPAGothic', 13, 'bold'))
        ''''''
        #self.isfilter.place(x = (self.winfo_reqwidth() -self.isfilter.winfo_reqwidth() -resetDATABtn.winfo_reqwidth()),
                            #y = (h -self.isfilter.winfo_reqheight()))
        '''

        #=================================================
        
        disp_var.set(0)

        ToolBarFrm4main = tk.Frame(self, relief = tk.RIDGE, bg = '#ffffff',
                                   width = (self['width'] -resetDATABtn.winfo_reqwidth()
                                            #-self.isfilter.winfo_reqwidth()
                                            ),
                                   height = 36, bd = 1)
        
        figH = self['height'] / figDpi
        figW = self['width'] / figDpi
        fig4main = Figure(figsize = (figW, figH), dpi = figDpi, facecolor='#ffffff')

        #================== 圖表區 ===========================
        otherfig = {}
        #================ ax4wave ==================
        otherfig['wave'] = {}
        axL = (90 * (figDpi/72))/self['width']
        axR = ((20 * (figDpi/72))/self['width']) *19.5
        axB = ((80 * (figDpi/72))/self['height']) *3.0
        axT = (25 * (figDpi/72))/self['height']
        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        otherfig['wave']['axes'] = fig4main.add_axes(axSize)
        #===========================================
        #================ ax4fft ===================
        otherfig['fft'] = {}
        axL = ((90 * (figDpi/72))/self['width']) *5.0
        axR = (20 * (figDpi/72))/self['width']
        axB = ((80 * (figDpi/72))/self['height']) *3.0
        axT = (25 * (figDpi/72))/self['height']
        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        otherfig['fft']['axes'] = fig4main.add_axes(axSize)
        #===========================================
        #================ ax4twmap =================
        otherfig['twmap'] = {}
        axL = ((90 * (figDpi/72))/self['width']) *5.0
        axR = (20 * (figDpi/72))/self['width']
        axB = ((80 * (figDpi/72))/self['height']) *1.15#*0.9375
        axT = ((25 * (figDpi/72))/self['height']) *6.9#*7.5
        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        otherfig['twmap']['axes'] = fig4main.add_axes(axSize)
        #===========================================
        self.def_til_font = FontProperties(fname = (rawS(curPath + '//msjhbd.ttc')))
        self.def_til_font.set_size(math.ceil(14*72/figDpi))
        self.def_til_font.set_weight('bold')
        otherfig['wave']['axes'].set_title(Config4Lan.get(AlarmCfg['lang'], 'WaveForm'), fontproperties = self.def_til_font, x = 0.13)
        otherfig['fft']['axes'].set_title(Config4Lan.get(AlarmCfg['lang'], 'FFT'), fontproperties = self.def_til_font, x = 0.13)
        otherfig['twmap']['axes'].set_title(Config4Lan.get(AlarmCfg['lang'], 'TF map'), fontproperties = self.def_til_font, x = 0.13)

        self.def_til_font = FontProperties(fname = (rawS(curPath + '//wqy-zenhei.ttc')))
        self.def_til_font.set_size(math.ceil(12*72/figDpi))
        self.def_til_font.set_weight('normal')
        otherfig['wave']['axes'].set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'Time'), fontproperties = self.def_til_font, x = 0.85, y = -0.08)
        otherfig['wave']['axes'].set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'amplitude'), fontproperties = self.def_til_font)
        otherfig['fft']['axes'].set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'freguence'), fontproperties = self.def_til_font, x = 0.85, y = -0.08)
        otherfig['fft']['axes'].set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'decibel'), fontproperties = self.def_til_font)
        otherfig['twmap']['axes'].set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'Equivalent Frequence'), fontproperties = self.def_til_font, x = 0.85, y = -0.08)
        otherfig['twmap']['axes'].set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'Equivalent Timelength'), fontproperties = self.def_til_font)

        otherfig['wave']['path'] = defaultdict(list)
        otherfig['fft']['path'] = defaultdict(list)
        otherfig['twmap']['path'] = defaultdict(list)
        for i in range(0, maxch4grp +1):
            if ((i >0) and (i <= len(GroupSet[viewGP]['ch']))):
                _lbl = ('%s%s' %(Config4Lan.get(AlarmCfg['lang'], 'channel'), GroupSet[viewGP]['ch'][i -1]))
            else:
                _lbl = ''

            otherfig['wave']['path'][i] = otherfig['wave']['axes'].plot([], [], '-', linewidth = 0.5,
                                                                        markersize = 1, label = _lbl)
            otherfig['fft']['path'][i] = otherfig['fft']['axes'].plot([], [], '-', linewidth = 0.5,
                                                                      markersize = 1, label = _lbl)
            otherfig['twmap']['path'][i] = otherfig['twmap']['axes'].plot([], [], 'o', ms = 4.0,
                                                                          label = _lbl)

        [otherfig[item]['axes'].grid() for item in otherfig]
        [otherfig[item]['axes'].set_visible(False) for item in otherfig]
        
        axL = (110 * (figDpi/72))/self['width']
        axR = ((20 * (figDpi/72))/self['width'])
        axB = ((80 * (figDpi/72))/self['height']) *1.05
        axT = ((25 * (figDpi/72))/self['height']) *1.1
        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        ax4main = fig4main.add_axes(axSize)  #left, bottom, width, height

        self.def_til_font = FontProperties(fname = (rawS(curPath + '//msjhbd.ttc')))
        self.def_til_font.set_size(math.ceil(20*72/figDpi))
        self.def_til_font.set_weight('bold')
        #'ax4main_til = OGHHLDCGOGGGBGAFLHGGDG'
        ax4main.set_title(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGAFLHGGDG'),
                          fontproperties = self.def_til_font, x = 0.13)

        self.def_til_font = FontProperties(fname = (rawS(curPath + '//wqy-zenhei.ttc')))
        self.def_til_font.set_size(math.ceil(16*72/figDpi))
        self.def_til_font.set_weight('normal')
        #'ax4mainXlbl = OGHHLDCGOGGGBGHFDGNGDG
        #'ax4mainYlbl = OGHHLDCGOGGGBGGFDGNGDG
        ax4main.set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGHFDGNGDG'),
                           fontproperties = self.def_til_font, x = 0.85, y = -0.08)
        ax4main.set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGGFDGNGDG'),
                           fontproperties = self.def_til_font)


        path4phas = Line2D([], [], color = "#000000", linestyle = '--', linewidth = 1)

        #================ 添加 PRPD path =========================================
        
        prpd4main = defaultdict(list)
        path4trig = defaultdict(list)
        for i in range(0, maxch4grp +1):
            if ((i >0) and (len(GroupSet) >0) and (i <= len(GroupSet[viewGP]['ch']))):
                _lbl = ('%s %s' %(Config4Lan.get(AlarmCfg['lang'], 'channel'), GroupSet[viewGP]['ch'][i -1]))
                '''
                _lbl = {
                    'zh-TW' : lambda : '通道%s' %GroupSet[viewGP]['ch'][i -1],
                    'en-US' : lambda : 'CH %s' %GroupSet[viewGP]['ch'][i -1],
                    }.get(AlarmCfg['lang'], lambda : '通道%s' %GroupSet[viewGP]['ch'][i -1])()
                '''
                self.data4main.update({i:{'x':[], 'y':[]}})
                self.data4twmap.update({i:{'x':[], 'y':[]}})
            else:
                _lbl = ''
            '''
            if ((i >0) and (i <= len(GroupSet[viewGP]['ch']))):
                _lbl = {
                    'zh-TW' : lambda : '通道%s' %GroupSet[viewGP]['ch'][i -1],
                    'en-US' : lambda : 'CH %s' %GroupSet[viewGP]['ch'][i -1],
                    }.get(AlarmCfg['lang'], lambda : '通道%s' %GroupSet[viewGP]['ch'][i -1])()
                self.data4main.update({i:{'x':[], 'y':[]}})
                self.data4twmap.update({i:{'x':[], 'y':[]}})
            else:
                _lbl = ''
            '''
            prpd4main[i] = ax4main.plot([], [], 'o', ms = 8.0, label = _lbl)

            if i >0:
                path4trig[i] = defaultdict(list)
                [path4trig[i].update({ j : Line2D([], [], color = prpd4main[i][0].get_color(), linestyle = '--', linewidth = 1)}) for j in (0, 1)]
                [ax4main.add_line(path4trig[i][j]) for j in (0, 1)]

        ax4main.add_line(path4phas)
        #print('prpd4main:', prpd4main)
        #prpd4main: defaultdict(<class 'list'>,
            #{0: [<matplotlib.lines.Line2D object at 0x000002BA877408D0>],
             #1: [<matplotlib.lines.Line2D object at 0x000002BA87740E10>],
             #2: [<matplotlib.lines.Line2D object at 0x000002BA87747B38>]})
        
        #print('path4trig:', path4trig)
        #path4trig: defaultdict(<class 'list'>,
            #{1: defaultdict(<class 'list'>,
                #{0: <matplotlib.lines.Line2D object at 0x0000021641736B38>,
                #1: <matplotlib.lines.Line2D object at 0x0000021641736CF8>}),
            #2: defaultdict(<class 'list'>,
                #{0: <matplotlib.lines.Line2D object at 0x000002164173E860>,
                #1: <matplotlib.lines.Line2D object at 0x000002164173EA20>})})
        
        '''
        path4trig = defaultdict(list)
        path4trig[0] = defaultdict(list)
        path4trig[1] = defaultdict(list)
        path4trig[0][0] = Line2D([], [], color = "#ff0000", linestyle = '--', linewidth = 1)
        path4trig[0][1] = Line2D([], [], color = "#ff0000", linestyle = '--', linewidth = 1)
        path4trig[1][0] = Line2D([], [], color = "#ff0000", linestyle = '--', linewidth = 1)
        path4trig[1][1] = Line2D([], [], color = "#ff0000", linestyle = '--', linewidth = 1)
        ax4main.add_line(path4trig[0])
        ax4main.add_line(path4trig[1])
        '''
        
        canvas4main = FigureCanvasTkAgg(fig4main, self)
        canvas4main.get_tk_widget().place(x = 0, y = 0)
        canvas4main._tkcanvas.place(x = 0, y = 0)

        global toolbar4main
        toolbar4main = CustomToolbar(canvas4main, self)
        toolbar4main.config(bg = "#ffffff")
        toolbar4main.place(x = (self.winfo_reqwidth() -toolbar4main.winfo_reqwidth()),
                           y = (h -toolbar4main.winfo_reqheight()))
        toolbar4main.update()
        ToolBarFrm4main.place(x = 0, y = self['height'] -ToolBarFrm4main['height'])
        ToolBarFrm4main.tkraise()
        resetDATABtn.tkraise()
        self.isfilter.tkraise()
        toolbar4main.tkraise()

        self.ang = list(range(0, 361,5))
        self.amp = [math.sin(math.radians(_a)) for _a in self.ang]
        path4phas.set_data(self.ang, self.amp)

        ax4main.set_autoscaley_on(True)
        ax4main.set_xlim([0, 360])
        ax4main.set_xticks(list(range(0, 361, 30)))

        ax4main.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
        self.def_til_font.set_size(math.ceil(14*72/figDpi))
        [label.set_fontproperties(self.def_til_font) for label in ax4main.get_xticklabels()]
        [label.set_fontproperties(self.def_til_font) for label in ax4main.get_yticklabels()]
        ax4main.grid()

        ax4main.relim()
        ax4main.autoscale_view()
        fig4main.canvas.draw()
        fig4main.canvas.flush_events()

        self.def_til_font.set_size(math.ceil(14*72/figDpi))
        self.def_til_font.set_weight('normal')
        
        if len(GroupSet) >0:
            self.updatechart()
            #self.timer = fig4main.canvas.new_timer(interval = int(AlarmCfg['period'] *1000))
            #self.timer = fig4main.canvas.new_timer(interval = 500)
            #self.timer.add_callback(self.updatechart)
            #self.timer.start()

        if self.law >0:
            loginlaw = GetGlobals('loginlaw')
            UpdateOptStates(self, int(self.law <= loginlaw))

    def chkfilter(self):
        global viewGP,GroupSet
        
        GroupSet = GetGlobals('GroupSet')
        GroupSet[viewGP]['isfilter'] = self.isfilter_var.get()
        UpdateGlobals('GroupSet', GroupSet)
        GroupSet = GetGlobals('GroupSet')
        
        db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
        db.execute("PRAGMA journal_mode=WAL")
        cursor  = db.cursor()
        cursor.execute('update adc_setting set isfilter = ? where sn = ?;', (self.isfilter_var.get(), viewGP))
        db.commit()
        cursor.close()
        db.close()
        pass

    def updatechart(self):
        #print('Mainfrm2.updatechart', time.time())
        global viewGP,GroupSet,tilBar,AlarmCfg,curPath,Config4Lan,path4trig,gainDict

        if self.isfilter_var.get() != GroupSet[viewGP]['isfilter']:
            self.isfilter_var.set(GroupSet[viewGP]['isfilter'])
            
        GroupSet = GetGlobals('GroupSet')

        if type(GroupSet[viewGP]['mmap']['prpd']) == mmap.mmap:
            _temp = array('f', GroupSet[viewGP]['mmap']['prpd'][:])
        else:
            _temp = []
            print('MainFrm2.updatechart', 'prpd')

        if len(_temp) >0:
            if disp_var.get() == 1:
            
                if type(GroupSet[viewGP]['mmap']['twmap']) == mmap.mmap:
                    _twmp = array('f', GroupSet[viewGP]['mmap']['twmap'][:])
                else:
                    _twmp = []
                    print('MainFrm2.updatechart', 'twmap')

                
                if type(GroupSet[viewGP]['mmap']['wave']) == mmap.mmap:
                    _wave = array('f', GroupSet[viewGP]['mmap']['wave'][:])
                else:
                    _wave = [0] *512 *2
                    print('MainFrm2.updatechart', 'wave')

                
                if type(GroupSet[viewGP]['mmap']['fft']) == mmap.mmap:
                    _fft = array('f', GroupSet[viewGP]['mmap']['fft'][:])
                else:
                    _fft = [0] *256 *2
                    print('MainFrm2.updatechart', 'fft')

            _gainary = [('00000000' +bin(GroupSet[viewGP]['gain'])[2:])[-8:][:4],
                        ('00000000' +bin(GroupSet[viewGP]['gain'])[2:])[-8:][-4:]]

            _maxAry = []
            _isrefresh = False
            for j in range(1, len(GroupSet[viewGP]['ch']) +1):
                jj = 2 *(j -1)
                _temp_x = [_temp[item] for item in list(range(jj, len(_temp), 4))
                           if _temp[item] != 65535.0 and _temp[item+1] != 65535.0]
                _temp_y = [_temp[item] for item in list(range(jj +1, len(_temp), 4))
                           if _temp[item -1] != 65535.0 and _temp[item] != 65535.0]

                #=======================================================================
                try:
                    _g = [_key for _key in gainDict if gainDict[_key][j -1] == _gainary[j -1]][0]
                except Exception as e:
                    #exc_type, exc_obj, exc_tb = sys.exc_info()
                    #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    #print(exc_type, fname, exc_tb.tb_lineno)
                    _g = '10x'

                _ig = int(_g[:2])
                #print('trig_lv:', GroupSet[viewGP]['trig_lv'], '_ig:', _ig)
                path4trig[j][0].set_data([0, 360], [(GroupSet[viewGP]['trig_lv'] /_ig), (GroupSet[viewGP]['trig_lv'] /_ig)])
                path4trig[j][1].set_data([0, 360], [-(GroupSet[viewGP]['trig_lv'] /_ig) , -(GroupSet[viewGP]['trig_lv'] /_ig)])
                #=======================================================================

                try:
                    _maxA = math.ceil(max([abs(prpd4main[j][0].get_ydata()[_i]) for _i in range(0, len(prpd4main[j][0].get_ydata()))]))
                except:
                    _maxA = 0

                _maxAry.append(_maxA)
                _maxAry.append((GroupSet[viewGP]['trig_lv'] /_ig))

                if len(prpd4main[j][0].get_ydata()) != len(_temp_y):
                    prpd4main[j][0].set_data(_temp_x, _temp_y)
                    '''
                    try:
                        _maxA = math.ceil(max([abs(prpd4main[j][0].get_ydata()[_i]) for _i in range(0, len(prpd4main[j][0].get_ydata()))]))
                    except:
                        _maxA = 0

                    _maxAry.append(_maxA)
                    _maxAry.append((GroupSet[viewGP]['trig_lv'] /_ig))
                    #if _maxA >self.maxA:
                        #self.maxA = _maxA
                    '''

                    del _temp_x,_temp_y
                    
                    if disp_var.get() == 1:

                        _twmp_x = [_twmp[item] for item in list(range(jj, len(_twmp), 4))
                                   if _twmp[item] != 65535.0 and _twmp[item+1] != 65535.0]
                        _twmp_y = [_twmp[item] for item in list(range(jj +1, len(_twmp), 4))
                                   if _twmp[item -1] != 65535.0 and _twmp[item] != 65535.0]
                        
                        _wave_y = _wave[((j -1) *512) : (((j -1) *512) +512)]
                        _wave_x = list(range(0, len(_wave_y)))
                        _fft_y = _fft[((j -1) *256) : (((j -1) *256) +256)]
                        _fft_x = [_j / (512 *0.008) for _j in range(0, 256)]    #list(range(0, len(_fft_y)))
                        otherfig['wave']['path'][j][0].set_data(_wave_x, _wave_y)
                        otherfig['fft']['path'][j][0].set_data(_fft_x, _fft_y)
                        otherfig['twmap']['path'][j][0].set_data(_twmp_x, _twmp_y)
                        del _twmp_x, _twmp_y, _wave_x, _wave_y, _fft_x, _fft_y

                        [otherfig[item]['axes'].relim() for item in otherfig]
                        [otherfig[item]['axes'].autoscale_view() for item in otherfig]

                    _isrefresh = True

            if _isrefresh:
                #print(_maxAry)
                if self.maxA != max(_maxAry):
                    self.maxA = max(_maxAry)
                    self.amp = [math.sin(math.radians(_a)) *self.maxA for _a in self.ang]
                    path4phas.set_data(self.ang, self.amp)

                ax4main.relim()
                ax4main.autoscale_view()
                fig4main.canvas.draw()
                self.refreshtime = time.time()
        '''
        if disp_var.get() == 1:
            [otherfig[item]['axes'].relim() for item in otherfig]
            [otherfig[item]['axes'].autoscale_view() for item in otherfig]

        ax4main.relim()
        ax4main.autoscale_view()
        fig4main.canvas.draw()
        '''

    def display_opt(self):
        global disp_var,ax4main,AlarmCfg,viewGP
        global path4phas,prpd4main,curPath,figDpi
        global otherfig,toolbar4main,root
        global maxch4grp,Config4Lan

        if disp_var.get() == 1:

            axL = (90 * (figDpi/72))/self['width']
            axR = ((20 * (figDpi/72))/self['width']) *19.5
            axB = ((80 * (figDpi/72))/self['height']) *1.15#*0.9375
            axT = ((25 * (figDpi/72))/self['height']) *6.9#*7.5
            ax4main.title.set_fontsize(math.ceil(14*72/figDpi))
            ax4main.xaxis.get_label().set_fontsize(math.ceil(12*72/figDpi))
            ax4main.yaxis.get_label().set_fontsize(math.ceil(12*72/figDpi))
            [otherfig[item]['axes'].set_visible(True) for item in otherfig]
            #[otherfig[item]['axes'].grid() for item in otherfig]
            [prpd4main[i][0].set_markersize(4.0) for i in range(0, len(prpd4main))]

            path4phas.set_linestyle('-')
            [ticklabel.set_fontsize(math.ceil(11*72/figDpi)) for ticklabel in ax4main.get_xticklabels()]
            [ticklabel.set_fontsize(math.ceil(11*72/figDpi)) for ticklabel in ax4main.get_yticklabels()]

            pass
        else:
            [otherfig[item]['axes'].set_visible(False) for item in otherfig]

            axL = (110 * (figDpi/72))/self['width']
            axR = (20 * (figDpi/72))/self['width']
            axB = ((80 * (figDpi/72))/self['height']) *1.05
            axT = ((25 * (figDpi/72))/self['height']) *1.1
            ax4main.xaxis.get_label().set_fontsize(math.ceil(16*72/figDpi))
            ax4main.yaxis.get_label().set_fontsize(math.ceil(16*72/figDpi))
            
            self.def_til_font.set_size(math.ceil(14*72/figDpi))
            self.def_til_font.set_weight('normal')
            [prpd4main[i][0].set_markersize(8.0) for i in range(0, len(prpd4main))]

            path4phas.set_linestyle('--')
            [ticklabel.set_fontsize(math.ceil(14*72/figDpi)) for ticklabel in ax4main.get_xticklabels()]
            [ticklabel.set_fontsize(math.ceil(14*72/figDpi)) for ticklabel in ax4main.get_yticklabels()]

            pass

        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        ax4main.set_position(axSize)

        ax4main.relim()
        ax4main.autoscale_view()
        fig4main.canvas.draw()
        #fig4main.canvas.flush_events()
        pass

    def SetCol_Rang(self, value):
        pass

#=================================================================
#========================= MainFrm2 =============================
'''
class MainFrm2(tk.Frame):
    def __init__(self, parent, controller, law):
        global curPath,tilBar,StatusBar,figDpi
        global AlarmCfg,disp_var,viewGP
        global fig4main,showgroup_var,ax4main
        global path4phas
        global chk_0_Img,chk_1_Img,Config4Lan

        tk.Frame.__init__(self,parent)
        h = parent['height'] -tilBar['height'] -StatusBar['height']
        self.config(relief = tk.GROOVE, bg = '#ffffff', width = parent['width'] -40, height = h)
        self.place(x = 0, y = tilBar['height'])
        self.law = law
        self.lasttime = time.time()
        self.maxA = 0.0
        #self.data4wave = {1:{'x':[], 'y':[]}, 2:{'x':[], 'y':[]}}
        #self.data4fft = {1:{'x':[], 'y':[]}, 2:{'x':[], 'y':[]}}
        self.data4main = {}
        self.data4twmap = {}


        self.icon4resetDATA = tk.PhotoImage(file = (curPath +"//trash2.png"))
        resetDATABtn = tk.Button(self, text='', font = ('IPAGothic', 13, 'bold'),
                                 image = self.icon4resetDATA, compound="center",
                                 command = lambda val = 1 : resetFunc(val))
                                 #command = lambda val = 1 : self.resetFunc(val))
        resetDATABtn.place(x = (self.winfo_reqwidth() -resetDATABtn.winfo_reqwidth()),
                           y = (h -resetDATABtn.winfo_reqheight()))


        #================= 濾波器 ==========================
        self.isfilter_var = tk.IntVar()
        self.isfilter_var.set(0)
        self.isfilter = tk.Checkbutton(self, variable = self.isfilter_var,
                                       bd = 0, relief = tk.FLAT, image = chk_0_Img,
                                       selectimage = chk_1_Img, onvalue = 1,
                                       offvalue = 0,
                                       command = self.chkfilter)
        self.isfilter.config(activebackground = "#ffffff",bg = "#ffffff", indicatoron  = 0)
        self.isfilter.config(compound = tk.LEFT, state = tk.NORMAL)
        #'isfilter = GGMHJGGGDGLHKGNH'
        self.isfilter.config(text = Config4Lan.get(AlarmCfg['lang'], 'GGMHJGGGDGLHKGNH'),
                             font = ('IPAGothic', 13, 'bold'))
        ''''''
        self.isfilter.config(text = {
            'zh-TW' : lambda : '濾波',
            'en-US' : lambda : 'Filter',
            }.get(AlarmCfg['lang'], lambda : '濾波')(),
                             font = ('IPAGothic', 13, 'bold'))
        ''''''
        #self.isfilter.place(x = (self.winfo_reqwidth() -self.isfilter.winfo_reqwidth() -resetDATABtn.winfo_reqwidth()),
                            #y = (h -self.isfilter.winfo_reqheight()))

        #=================================================
        
        disp_var.set(0)

        ToolBarFrm4main = tk.Frame(self, relief = tk.RIDGE, bg = '#ffffff',
                                   width = (self['width'] -resetDATABtn.winfo_reqwidth() -self.isfilter.winfo_reqwidth()),
                                   height = 36, bd = 1)
        
        figH = self['height'] / figDpi
        figW = self['width'] / figDpi
        fig4main = Figure(figsize = (figW, figH), dpi = figDpi, facecolor='#ffffff')

        axL = (60 * (figDpi/72))/self['width']
        axR = (20 * (figDpi/72))/self['width']
        axB = ((80 * (figDpi/72))/self['height']) *1.05
        axT = ((25 * (figDpi/72))/self['height']) *1.1
        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        ax4main = fig4main.add_axes(axSize)  #left, bottom, width, height

        self.def_til_font = FontProperties(fname = (rawS(curPath + '//msjhbd.ttc')))
        self.def_til_font.set_size(math.ceil(20*72/figDpi))
        self.def_til_font.set_weight('bold')
        #'ax4main_til = OGHHLDCGOGGGBGAFLHGGDG'
        ax4main.set_title(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGAFLHGGDG'),
                          fontproperties = self.def_til_font, x = 0.13)
        ''''''
        {
            'zh-TW' : lambda : ax4main.set_title(u'相位 vs 放電量', fontproperties = self.def_til_font, x = 0.13),
            'en-US' : lambda : ax4main.set_title(u'Phase vs PD', fontproperties = self.def_til_font, x = 0.13),
            }.get(AlarmCfg['lang'], lambda : ax4main.set_title(u'相位 vs 放電量', fontproperties = self.def_til_font, x = 0.13))()
        ''''''

        self.def_til_font = FontProperties(fname = (rawS(curPath + '//wqy-zenhei.ttc')))
        self.def_til_font.set_size(math.ceil(16*72/figDpi))
        self.def_til_font.set_weight('normal')
        #'ax4mainXlbl = OGHHLDCGOGGGBGHFDGNGDG
        #'ax4mainYlbl = OGHHLDCGOGGGBGGFDGNGDG
        ax4main.set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGHFDGNGDG'),
                           fontproperties = self.def_til_font, x = 0.85, y = -0.08)
        ax4main.set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGGFDGNGDG'),
                           fontproperties = self.def_til_font)
        ''''''
        {
            'zh-TW' : lambda : (ax4main.set_xlabel(u'相位 (°)', fontproperties = self.def_til_font, x = 0.85, y = -0.08),
                                ax4main.set_ylabel(u'放電量(mv)', fontproperties = self.def_til_font)),
            'en-US' : lambda : (ax4main.set_xlabel(u'Phase (°)', fontproperties = self.def_til_font, x = 0.85, y = -0.08),
                                ax4main.set_ylabel(u'PD (mv)', fontproperties = self.def_til_font)),
            }.get(AlarmCfg['lang'], lambda : (ax4main.set_xlabel(u'相位 (°)', fontproperties = self.def_til_font, x = 0.85, y = -0.08),
                                              ax4main.set_ylabel(u'放電量(mv)', fontproperties = self.def_til_font)))()
        ''''''

        path4phas = Line2D([], [], color = "#000000", linestyle = '--', linewidth = 1)

        #================ 添加 PRPD path =========================================
        global prpd4main,maxch4grp
        prpd4main = defaultdict(list)
        for i in range(0, maxch4grp +1):
            if ((i >0) and (len(GroupSet) >0) and (i <= len(GroupSet[viewGP]['ch']))):
                _lbl = ('%s %s' %(Config4Lan.get(AlarmCfg['lang'], 'channel'), GroupSet[viewGP]['ch'][i -1]))
                ''''''
                _lbl = {
                    'zh-TW' : lambda : '通道%s' %GroupSet[viewGP]['ch'][i -1],
                    'en-US' : lambda : 'CH %s' %GroupSet[viewGP]['ch'][i -1],
                    }.get(AlarmCfg['lang'], lambda : '通道%s' %GroupSet[viewGP]['ch'][i -1])()
                ''''''
                self.data4main.update({i:{'x':[], 'y':[]}})
                self.data4twmap.update({i:{'x':[], 'y':[]}})
            else:
                _lbl = ''
            ''''''
            if ((i >0) and (i <= len(GroupSet[viewGP]['ch']))):
                _lbl = {
                    'zh-TW' : lambda : '通道%s' %GroupSet[viewGP]['ch'][i -1],
                    'en-US' : lambda : 'CH %s' %GroupSet[viewGP]['ch'][i -1],
                    }.get(AlarmCfg['lang'], lambda : '通道%s' %GroupSet[viewGP]['ch'][i -1])()
                self.data4main.update({i:{'x':[], 'y':[]}})
                self.data4twmap.update({i:{'x':[], 'y':[]}})
            else:
                _lbl = ''
            ''''''
            prpd4main[i] = ax4main.plot([], [], 'o', ms = 8.0, label = _lbl)
        
        ax4main.add_line(path4phas)
        
        canvas4main = FigureCanvasTkAgg(fig4main, self)
        canvas4main.get_tk_widget().place(x = 0, y = 0)
        canvas4main._tkcanvas.place(x = 0, y = 0)

        global toolbar4main
        toolbar4main = CustomToolbar(canvas4main, self)
        toolbar4main.config(bg = "#ffffff")
        toolbar4main.place(x = (self.winfo_reqwidth() -toolbar4main.winfo_reqwidth()),
                           y = (h -toolbar4main.winfo_reqheight()))
        toolbar4main.update()
        ToolBarFrm4main.place(x = 0, y = self['height'] -ToolBarFrm4main['height'])
        ToolBarFrm4main.tkraise()
        resetDATABtn.tkraise()
        self.isfilter.tkraise()
        toolbar4main.tkraise()

        self.ang = list(range(0, 361,5))
        self.amp = [math.sin(math.radians(_a)) for _a in self.ang]
        path4phas.set_data(self.ang, self.amp)

        ax4main.set_autoscaley_on(True)
        ax4main.set_xlim([0, 360])
        ax4main.set_xticks(list(range(0, 361, 30)))

        ax4main.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
        self.def_til_font.set_size(math.ceil(14*72/figDpi))
        [label.set_fontproperties(self.def_til_font) for label in ax4main.get_xticklabels()]
        [label.set_fontproperties(self.def_til_font) for label in ax4main.get_yticklabels()]
        ax4main.grid()

        ax4main.relim()
        ax4main.autoscale_view()
        fig4main.canvas.draw()
        fig4main.canvas.flush_events()

        self.def_til_font.set_size(math.ceil(14*72/figDpi))
        self.def_til_font.set_weight('normal')

        if len(GroupSet) >0:
            self.updatechart()
            self.timer = fig4main.canvas.new_timer(interval = int(AlarmCfg['period'] *1000))
            #self.timer = fig4main.canvas.new_timer(interval = 500)
            self.timer.add_callback(self.updatechart)
            self.timer.start()

        if self.law >0:
            loginlaw = GetGlobals('loginlaw')
            UpdateOptStates(self, int(self.law <= loginlaw))

    def chkfilter(self):
        global viewGP,GroupSet
        
        GroupSet = GetGlobals('GroupSet')
        GroupSet[viewGP]['isfilter'] = self.isfilter_var.get()
        UpdateGlobals('GroupSet', GroupSet)
        GroupSet = GetGlobals('GroupSet')
        
        db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
        db.execute("PRAGMA journal_mode=WAL")
        cursor  = db.cursor()
        cursor.execute('update adc_setting set isfilter = ? where sn = ?;', (self.isfilter_var.get(), viewGP))
        db.commit()
        cursor.close()
        db.close()
        pass

    def updatechart(self):
        global viewGP,GroupSet,tilBar,AlarmCfg,curPath,Config4Lan
        #if self.lasttime != os.stat((curPath +('//prpd_g%s.~' %viewGP))).st_mtime:
        #if  self.lasttime != GroupSet[viewGP]['triglist']:
        if self.isfilter_var.get() != GroupSet[viewGP]['isfilter']:
            self.isfilter_var.set(GroupSet[viewGP]['isfilter'])
            
        GroupSet = GetGlobals('GroupSet')
        _temp = []
        if type(GroupSet[viewGP]['mmap']['prpd']) == mmap.mmap:
            _temp = array('f', GroupSet[viewGP]['mmap']['prpd'][:])

        if disp_var.get() == 1:
            _twmp = []
            if type(GroupSet[viewGP]['mmap']['twmap']) == mmap.mmap:
                _twmp = array('f', GroupSet[viewGP]['mmap']['twmap'][:])

            _wave = [0] *512 *2
            if type(GroupSet[viewGP]['mmap']['wave']) == mmap.mmap:
                _wave = array('f', GroupSet[viewGP]['mmap']['wave'][:])

            _fft = [0] *256 *2
            if type(GroupSet[viewGP]['mmap']['fft']) == mmap.mmap:
                _fft = array('f', GroupSet[viewGP]['mmap']['fft'][:])

        for j in range(1, len(GroupSet[viewGP]['ch']) +1):
            jj = 2 *(j -1)
            _temp_x = [_temp[item] for item in list(range(jj, len(_temp), 4))
                       if _temp[item] != 65535.0 and _temp[item+1] != 65535.0]
            _temp_y = [_temp[item] for item in list(range(jj +1, len(_temp), 4))
                       if _temp[item -1] != 65535.0 and _temp[item] != 65535.0]

            if len(prpd4main[j][0].get_ydata()) != len(_temp_y):
                prpd4main[j][0].set_data(_temp_x, _temp_y)

                try:
                    _maxA = math.ceil(max([abs(prpd4main[j][0].get_ydata()[_i]) for _i in range(0, len(prpd4main[j][0].get_ydata()))]))
                except:
                    _maxA = 0
                if _maxA >self.maxA:
                    self.maxA = _maxA

                del _temp_x,_temp_y
                
                if disp_var.get() == 1:

                    _twmp_x = [_twmp[item] for item in list(range(jj, len(_twmp), 4))
                               if _twmp[item] != 65535.0 and _twmp[item+1] != 65535.0]
                    _twmp_y = [_twmp[item] for item in list(range(jj +1, len(_twmp), 4))
                               if _twmp[item -1] != 65535.0 and _twmp[item] != 65535.0]
                    
                    _wave_y = _wave[((j -1) *512) : (((j -1) *512) +512)]
                    _wave_x = list(range(0, len(_wave_y)))
                    _fft_y = _fft[((j -1) *256) : (((j -1) *256) +256)]
                    _fft_x = list(range(0, len(_fft_y)))
                    otherfig['wave']['path'][j][0].set_data(_wave_x, _wave_y)
                    otherfig['fft']['path'][j][0].set_data(_fft_x, _fft_y)
                    otherfig['twmap']['path'][j][0].set_data(_twmp_x, _twmp_y)
                    del _twmp_x, _twmp_y, _wave_x, _wave_y, _fft_x, _fft_y

                if self.maxA >= max(self.amp):
                    self.amp = [math.sin(math.radians(_a)) *self.maxA for _a in self.ang]
                    path4phas.set_data(self.ang, self.amp)


        if disp_var.get() == 1:
            [otherfig[item]['axes'].relim() for item in otherfig]
            [otherfig[item]['axes'].autoscale_view() for item in otherfig]

        ax4main.relim()
        ax4main.autoscale_view()
        fig4main.canvas.draw()

    def display_opt(self):
        global disp_var,ax4main,AlarmCfg,viewGP
        global path4phas,prpd4main,curPath,figDpi
        global otherfig,toolbar4main,root
        global maxch4grp,Config4Lan

        if disp_var.get() == 1:
            otherfig = {}
            #================ ax4wave ==================
            otherfig['wave'] = {}
            axL = (60 * (figDpi/72))/self['width']
            axR = ((20 * (figDpi/72))/self['width']) *19.5
            axB = ((80 * (figDpi/72))/self['height']) *3.0
            axT = (25 * (figDpi/72))/self['height']
            axW = 1 - axL - axR
            axH = 1 - axT - axB
            axSize = [axL, axB, axW, axH]
            otherfig['wave']['axes'] = fig4main.add_axes(axSize)
            #===========================================
            #================ ax4fft ===================
            otherfig['fft'] = {}
            axL = ((60 * (figDpi/72))/self['width']) *7.1
            axR = (20 * (figDpi/72))/self['width']
            axB = ((80 * (figDpi/72))/self['height']) *3.0
            axT = (25 * (figDpi/72))/self['height']
            axW = 1 - axL - axR
            axH = 1 - axT - axB
            axSize = [axL, axB, axW, axH]
            otherfig['fft']['axes'] = fig4main.add_axes(axSize)
            #===========================================
            #================ ax4twmap =================
            otherfig['twmap'] = {}
            axL = ((60 * (figDpi/72))/self['width']) *7.1
            axR = (20 * (figDpi/72))/self['width']
            axB = ((80 * (figDpi/72))/self['height']) *1.15#*0.9375
            axT = ((25 * (figDpi/72))/self['height']) *6.9#*7.5
            axW = 1 - axL - axR
            axH = 1 - axT - axB
            axSize = [axL, axB, axW, axH]
            otherfig['twmap']['axes'] = fig4main.add_axes(axSize)
            #===========================================
            self.def_til_font = FontProperties(fname = (rawS(curPath + '//msjhbd.ttc')))
            self.def_til_font.set_size(math.ceil(14*72/figDpi))
            self.def_til_font.set_weight('bold')
            otherfig['wave']['axes'].set_title(Config4Lan.get(AlarmCfg['lang'], 'WaveForm'), fontproperties = self.def_til_font, x = 0.13)
            otherfig['fft']['axes'].set_title(Config4Lan.get(AlarmCfg['lang'], 'FFT'), fontproperties = self.def_til_font, x = 0.13)
            otherfig['twmap']['axes'].set_title(Config4Lan.get(AlarmCfg['lang'], 'TF map'), fontproperties = self.def_til_font, x = 0.13)

            self.def_til_font = FontProperties(fname = (rawS(curPath + '//wqy-zenhei.ttc')))
            self.def_til_font.set_size(math.ceil(12*72/figDpi))
            self.def_til_font.set_weight('normal')
            otherfig['wave']['axes'].set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'Time'), fontproperties = self.def_til_font, x = 0.85, y = -0.08)
            otherfig['wave']['axes'].set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'amplitude'), fontproperties = self.def_til_font)
            otherfig['fft']['axes'].set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'freguence'), fontproperties = self.def_til_font, x = 0.85, y = -0.08)
            otherfig['fft']['axes'].set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'decibel'), fontproperties = self.def_til_font)
            otherfig['twmap']['axes'].set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'Equivalent Frequence'), fontproperties = self.def_til_font, x = 0.85, y = -0.08)
            otherfig['twmap']['axes'].set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'Equivalent Timelength'), fontproperties = self.def_til_font)

            otherfig['wave']['path'] = defaultdict(list)
            otherfig['fft']['path'] = defaultdict(list)
            otherfig['twmap']['path'] = defaultdict(list)
            for i in range(0, maxch4grp +1):
                if ((i >0) and (i <= len(GroupSet[viewGP]['ch']))):
                    _lbl = ('%s%s' %(Config4Lan.get(AlarmCfg['lang'], 'channel'), GroupSet[viewGP]['ch'][i -1]))
                    ''''''
                    _lbl = {
                        'zh-TW' : lambda : '通道%s' %GroupSet[viewGP]['ch'][i -1],
                        'en-US' : lambda : 'CH %s' %GroupSet[viewGP]['ch'][i -1],
                        }.get(AlarmCfg['lang'], lambda : '通道%s' %GroupSet[viewGP]['ch'][i -1])()
                    ''''''
                else:
                    _lbl = ''

                otherfig['wave']['path'][i] = otherfig['wave']['axes'].plot([], [], '-', linewidth = 0.5,
                                                                            markersize = 1, label = _lbl)
                otherfig['fft']['path'][i] = otherfig['fft']['axes'].plot([], [], '-', linewidth = 0.5,
                                                                          markersize = 1, label = _lbl)
                otherfig['twmap']['path'][i] = otherfig['twmap']['axes'].plot([], [], 'o', ms = 4.0,
                                                                              label = _lbl)

            axL = (60 * (figDpi/72))/self['width']
            axR = ((20 * (figDpi/72))/self['width']) *19.5
            axB = ((80 * (figDpi/72))/self['height']) *1.15#*0.9375
            axT = ((25 * (figDpi/72))/self['height']) *6.9#*7.5
            ax4main.title.set_fontsize(math.ceil(14*72/figDpi))
            ax4main.xaxis.get_label().set_fontsize(math.ceil(12*72/figDpi))
            ax4main.yaxis.get_label().set_fontsize(math.ceil(12*72/figDpi))

            [otherfig[item]['axes'].grid() for item in otherfig]
            [prpd4main[i][0].set_markersize(4.0) for i in range(0, len(prpd4main))]

            pass
        else:
            [otherfig[item]['axes'].remove() for item in otherfig]
            del otherfig

            axL = (60 * (figDpi/72))/self['width']
            axR = (20 * (figDpi/72))/self['width']
            axB = ((80 * (figDpi/72))/self['height']) *1.05
            axT = ((25 * (figDpi/72))/self['height']) *1.1

            ax4main.title.set_fontsize(math.ceil(20*72/figDpi))
            ax4main.xaxis.get_label().set_fontsize(math.ceil(16*72/figDpi))
            ax4main.yaxis.get_label().set_fontsize(math.ceil(16*72/figDpi))
            
            self.def_til_font.set_size(math.ceil(14*72/figDpi))
            self.def_til_font.set_weight('normal')
            [prpd4main[i][0].set_markersize(8.0) for i in range(0, len(prpd4main))]

            pass

        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        ax4main.set_position(axSize)

        if disp_var.get() == 1:
            path4phas.set_linestyle('-')
            [ticklabel.set_fontsize(math.ceil(11*72/figDpi)) for ticklabel in ax4main.get_xticklabels()]
            [ticklabel.set_fontsize(math.ceil(11*72/figDpi)) for ticklabel in ax4main.get_yticklabels()]
        else:
            path4phas.set_linestyle('--')
            [ticklabel.set_fontsize(math.ceil(14*72/figDpi)) for ticklabel in ax4main.get_xticklabels()]
            [ticklabel.set_fontsize(math.ceil(14*72/figDpi)) for ticklabel in ax4main.get_yticklabels()]
        
        ax4main.relim()
        ax4main.autoscale_view()
        fig4main.canvas.draw()
        #fig4main.canvas.flush_events()
        pass

    def SetCol_Rang(self, value):
        pass
'''
#=================================================================
#========================== Trend Frame ===============================
class TrendFrm(tk.Frame):
    def __init__(self, parent, controller, law):
        global tilBar,StatusBar,fig4trend,ax4trend,ax4mv,def_til_font,AlarmCfg
        global showgroup_var,chx_sel,figDpi,thisOS,disp_var,Config4Lan
        tk.Frame.__init__(self,parent)
        h = parent['height'] -tilBar['height'] -StatusBar['height']
        self.config(relief = tk.GROOVE, bg = '#ffffff', width = parent['width'] -40, height = h)
        self.place(x = 0, y = tilBar['height'])        #self.pi = self.place_info()
        self.law = law
        self.legend = None
        self.refreshtime = 0.0

        self.ToolBarFrm4trend = tk.Frame(self, relief = tk.RIDGE, bg = '#ffffff', width = self['width'], height = 36, bd = 1)

        self.TimeInv_variable = tk.StringVar()
        #self.OPTION_TUPLE4trend = ("10 分",)
        #self.OPTION_TUPLE4trend = {
            #'zh-TW' : lambda : ("10 分",),
            #'en-US' : lambda : ("10 Min.",),
            #}.get(AlarmCfg['lang'], lambda : ("10 分",))()
        #self.TimeInv_variable.set(self.OPTION_TUPLE4trend[0])
        
        #'TimeInvDict : LFGGCGKGGEBGJHLEGGMGLH'
        _ary = Config4Lan.get(AlarmCfg['lang'], 'LFGGCGKGGEBGJHLEGGMGLH').split(';')
        self.TimeInvDict = {}
        [self.TimeInvDict.update({i :{'Label': {AlarmCfg['lang'] : _ary[i]}, 'interval': float(_ary[i][:3])}}) for i in range(0, len(_ary))]
        self.OPTION_TUPLE4trend = [self.TimeInvDict[i]['Label'] for i in self.TimeInvDict]
        '''
        self.TimeInvDict = {
            0 : {'Label': {'zh-TW' : '10 分', 'en-US' : '10Min.', 'zh-CN' : '10 分'}, 'interval' : 10.0},
            1 : {'Label': {'zh-TW' : ' 1分', 'en-US' : ' 1Min.', 'zh-CN' : '1 分'}, 'interval' : 1.0}}    #unit: Min.
        self.OPTION_TUPLE4trend = [self.TimeInvDict[i]['Label'][AlarmCfg['lang']] for i in self.TimeInvDict]
        '''

        self.TimeInvFrm = tk.Frame(self, relief = tk.RIDGE, bg = '#ffffff',
                                   bd = 1)
        self.TimeInvBtn = tk.Label(self.TimeInvFrm, textvariable = self.TimeInv_variable,
                                   relief = tk.RAISED, bd = 2, width = 6, height = 1,
                                   font = ('IPAGothic', 10, 'bold'))
        self.TimeInvBtn.grid(r        self.TimeInvLbl = tk.Label(self.TimeInvFrm)
        self.TimeInvLbl_variable = tk.StringVar()
        self.TimeInvLbl_variable.set(Config4Lan.get(AlarmCfg['lang'], 'Interval'))
        '''
        self.TimeInvLbl_variable.set(
            {
                'zh-TW' : lambda : '統計區間',
                'en-US' : lambda : 'Interval',
                }.get(AlarmCfg['lang'], lambda : '統計區間')())
        '''
        self.TimeInvLbl.config(textvariable = self.TimeInvLbl_variable, font = ('IPAGothic', 13, 'bold'))
        self.TimeInvLbl.config(bg = '#ffffff', relief = tk.FLAT)
        self.TimeInvLbl.grid(row = 0, column = 0)
        self.TimeInvFrm.update()
        self.TimeInvFrm.place(x = (self.winfo_reqwidth() -self.TimeInvFrm.winfo_reqwidth()),
                              y = 0)

        self.snlbl = tk.Label(self.ToolBarFrm4trend, relief = tk.FLAT,
                              bg = '#ffffff', fg = '#0000ff', bd = 0)
        self.snlbl.config(text = 'SN:', font = ('IPAGothic', 13, 'bold'))

        self.sn_var = tk.StringVar()
        self.sn_var.set(getsn())
        self.sn = tk.Label(self.ToolBarFrm4trend, textvariable = self.sn_var,
                            font = ('IPAGothic', 16, 'bold'), bg = '#ffffff',
                            fg = '#0000ff', compound = tk.LEFT)

        self.snlbl.place(x = (self.ToolBarFrm4trend.winfo_reqwidth() -
                              self.snlbl.winfo_reqwidth() -
                              self.sn.winfo_reqwidth()),
                         y = 5)
        self.sn.place(x = self.ToolBarFrm4trend.winfo_reqwidth() -self.sn.winfo_reqwidth(), y = 0)

        #======================= 圖表區 ======================
        figH = self['height'] / figDpi
        figW = self['width'] / figDpi
        axL = ((100 * (figDpi/72))/self['width'])# *1.0
        axR = ((80 * (figDpi/72))/self['width'])# *1.5
        axB = ((80 * (figDpi/72))/self['height']) *2.7
        axT = ((25 * (figDpi/72))/self['height']) *1.4
        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        self.fig4trend = Figure(figsize = (figW, figH), dpi = figDpi, facecolor='#ffffff')
        self.ax4trend = self.fig4trend.add_axes(axSize)  #left, bottom, width, height

        axL = ((100 * (figDpi/72))/self['width'])# *1.0
        axR = ((80 * (figDpi/72))/self['width'])# *1.5
        axB = ((80 * (figDpi/72))/self['height']) *1.0625
        axT = ((25 * (figDpi/72))/self['height']) *6.6

        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        self.ax4mv = self.fig4trend.add_axes(axSize)  #left, bottom, width, height

        self.def_til_font = FontProperties(fname = rawS(curPath + '//wqy-zenhei.ttc'))
        
        self.canvas4trend = FigureCanvasTkAgg(self.fig4trend, self)
        self.canvas4trend.get_tk_widget().place(x = 0, y = 0)
        self.canvas4trend._tkcanvas.place(x = 0, y = 0)

        self.updateInv = [self.TimeInvDict[i]['interval'] for i in self.TimeInvDict
                          if self.TimeInvDict[i]['Label'][AlarmCfg['lang']] == self.TimeInv_variable.get()][0]

        self.toolbar4trend = CustomToolbar(self.canvas4trend, self)
        self.toolbar4trend.config(bg = "#ffffff")
        self.toolbar4trend.place(x = (self.winfo_reqwidth() -self.toolbar4trend.winfo_reqwidth()),
                                 y = (h -self.toolbar4trend.winfo_reqheight()))
        self.toolbar4trend.update()
        self.ToolBarFrm4trend.place(x = 0, y = (self['height'] - self.ToolBarFrm4trend['height']))
        self.ToolBarFrm4trend.tkraise()
        
        self.TimeInvFrm.tkraise()
        #TimeInvLbl.tkraise()
        #TimeInvBtn.tkraise()
        self.toolbar4trend.tkraise()
        drawchart4trend(self, AlarmCfg['lang'])
        if len(GroupSet) >0:
            self.drawchart4trend()

            '''
            self.timer = self.fig4trend.canvas.new_timer(interval = 1000)
            self.timer.add_callback(self.updateChart)
            self.timer.start()
            self.updateChart()
            '''
            
        if self.law >0:
            loginlaw = GetGlobals('loginlaw')
            UpdateOptStates(self, int(self.law <= loginlaw))

    def updateChart(self):
        global AlarmCfg,maxch4grp,GroupSet,viewGP,path4trend,path4mv

        _xmax = math.ceil(time.time()/ (self.updateInv *60))	#local timestamp Unit:min
        _xmax = _xmax *self.updateInv *60     #local timestamp Unit: sec
        if _xmax > self.xmax:       #update axis-x scale
            self.xmax = _xmax
            _xmax = datetime.datetime.fromtimestamp(self.xmax)
            _xmin = _xmax +datetime.timedelta(days = -1)

            self.ax4trend.set_xlim([_xmin, _xmax])
            self.ax4mv.set_xlim([_xmin, _xmax])
            self.ax4trend.set_xticklabels([])

        _isChk = reduce(lambda x, y: x *y, [type(GroupSet[viewGP]['trend'][x]['fd']) == mmap.mmap for x in GroupSet[viewGP]['trend'].keys()])
        if _isChk >0:
            for key in GroupSet[viewGP]['trend'].keys():
                nrec = int(GroupSet[viewGP]['trend'][key]['fd'].size() /12)
                _temp = struct.unpack('Iff' *nrec, GroupSet[viewGP]['trend'][key]['fd'][:])
                for i in range(0, maxch4grp +1):
                    if i ==0:
                        pass
                    else:
                        if i <= len(GroupSet[viewGP]['ch']):
                            BarArray = [_temp[item] for item in range(0, len(_temp), 3)]
            self.ax4mv.set_autoscaley_on(True)
            self.ax4trend.relim()
            self.ax4mv.relim()
            self.ax4trend.autoscale_view()
            self.ax4mv.autoscale_view()
            self.fig4trend.canvas.draw()
            self.refreshtime = time.time()

        '''
        for i in range(0, maxch4grp +1):

            if i ==0:
                pass
            else:
                if i <= len(GroupSet[viewGP]['ch']):
                    _key = list(GroupSet[viewGP]['trend']['mv'][i -1].keys())
                    BarArray = [datetime.datetime.fromtimestamp(float(key)) for key in _key
                                #if type(GroupSet[viewGP]['trend']['mv'][i -1][key]) != collections.deque
                                ]
                    ydata1 = [GroupSet[viewGP]['trend']['mv'][i -1][key] for key in _key
                              #if type(GroupSet[viewGP]['trend']['mv'][i -1][key]) != collections.deque
                              ]
                    _tmp = [ik for ik in range(0, len(_key))
                            if type(GroupSet[viewGP]['trend']['mv'][i -1][(_key[ik])]) == collections.deque
                            ]
                    if len(_tmp) >0:
                        for ik in _tmp:
                            #print(len(_key), ik)
                            if len(GroupSet[viewGP]['trend']['mv'][i -1][_key[ik]]) >0:
                                _meanV = np.mean(GroupSet[viewGP]['trend']['mv'][i -1][_key[ik]])
                            else:
                                _meanV = 0.0
                            ydata1[ik] = _meanV

                    path4mv[i].set_data(BarArray, ydata1)
                    del ydata1

                    ydata1 = [GroupSet[viewGP]['trend']['counters'][i -1][key] for key in _key]
                    path4trend[i].set_data(BarArray, ydata1)
                    del _key, BarArray, ydata1
        '''
                    
        '''
                    _key = list(GroupSet[viewGP]['trend']['counters'][i -1].keys())
                    BarArray = [datetime.datetime.fromtimestamp(float(key)) for key in _key]
                    ydata1 = [GroupSet[viewGP]['trend']['counters'][i -1][key] for key in GroupSet[viewGP]['trend']['counters'][i -1].keys()]
                    path4trend[i].set_data(BarArray, ydata1)
                    
                    _key = list(GroupSet[viewGP]['trend']['mv'][i -1].keys())
                    BarArray = [datetime.datetime.fromtimestamp(float(key)) for key in _key]
                    ydata1 = []
                    if len(_key) >=2:
                        ydata1 = [GroupSet[viewGP]['trend']['mv'][i -1][key] for key in _key[:-1]]
                        if type(GroupSet[viewGP]['trend']['mv'][i -1][_key[-1]]) == collections.deque:
                            if len(GroupSet[viewGP]['trend']['mv'][i -1][_key[-1]]) >0:
                                _meanV = np.mean(GroupSet[viewGP]['trend']['mv'][i -1][_key[-1]])
                            else:
                                _meanV = 0.0
                        else:
                            _meanV = GroupSet[viewGP]['trend']['mv'][i -1][_key[-1]]
                            pass
                        ydata1.append(_meanV)
                    elif len(_key) == 1:
                        if type(GroupSet[viewGP]['trend']['mv'][i -1][_key[-1]]) == collections.deque:
                            if len(GroupSet[viewGP]['trend']['mv'][i -1][_key[-1]]) >0:
                                _meanV = np.mean(GroupSet[viewGP]['trend']['mv'][i -1][_key[-1]])
                            else:
                                _meanV = 0.0
                        else:
                            _meanV = GroupSet[viewGP]['trend']['mv'][i -1][_key[-1]]
                            pass
                        ydata1.append(_meanV)
                    else:
                        pass
                    path4mv[i].set_data(BarArray, ydata1)
        '''
        '''
        self.ax4trend.set_autoscaley_on(True)
        self.ax4mv.set_autoscaley_on(True)
        self.ax4trend.relim()
        self.ax4mv.relim()
        self.ax4trend.autoscale_view()
        self.ax4mv.autoscale_view()
        self.fig4trend.canvas.draw()
        #self.fig4trend.canvas.flush_events()
        '''
        pass

    def drawchart4trend(self):
        global AlarmCfg#,Ch_Status,figDpi,maxch4grp
        global GroupSet,viewGP,path4trend,path4mv

        _inv = [self.TimeInvDict[i]['interval'] for i in self.TimeInvDict
                if self.TimeInvDict[i]['Label'][AlarmCfg['lang']] == self.TimeInv_variable.get()][0]

        _xmax = math.ceil(time.time()/ (_inv *60))	#local timestamp Unit:min
        _xmax = _xmax *_inv *60     #local timestamp Unit: sec
        self.xmax = _xmax
        _xmax = datetime.datetime.fromtimestamp(self.xmax)
        _xmin = _xmax +datetime.timedelta(days = -1)

        path4trend = defaultdict(list)
        path4mv = defaultdict(list)
        lpath = []
        lpath2 = []
        legend_txt = []
        legend_txt2 = []

        for i in range(0, maxch4grp +1):
            if i ==0:
                '''
                if (len(GroupSet[viewGP]['ch'])) >= 2:
                    _lbl = {
                        'zh-TW' : lambda : ('通道('+
                                            ('&'.join(str(x) for x in GroupSet[viewGP]['ch']))+
                                            ')'),
                        'en-US' : lambda : ('Ch('+
                                            ('&'.join(str(x) for x in GroupSet[viewGP]['ch']))+
                                            ')'),
                        }.get(AlarmCfg['lang'], lambda : ('通道('+
                                                          ('&'.join(str(x) for x in GroupSet[viewGP]['ch']))+
                                                          ')')
                              )()
                    pass
                else:
                    _lbl = ''
                '''
                _lbl = ''
                pass
            else:
                if i <= len(GroupSet[viewGP]['ch']):
                    _lbl = ('%s %s' %(Config4Lan.get(AlarmCfg['lang'], 'channel'), GroupSet[viewGP]['ch'][i -1]))
                    '''
                    _lbl = {
                        'zh-TW' : lambda : ('通道 %s' %(GroupSet[viewGP]['ch'][i -1])),
                        'en-US' : lambda : ('Ch %s' %(GroupSet[viewGP]['ch'][i -1])),
                        }.get(AlarmCfg['lang'], lambda : ('通道 %s' %(GroupSet[viewGP]['ch'][i -1]))
                              )()
                    '''
                    #['#ff7f0e', '#2ca02c']
                    path4mv[i] = Line2D([], [], color = prpd4main[i][0].get_color(), label = _lbl, linewidth = 2)
                    lpath2.append(path4mv[i])
                    self.ax4mv.add_line(path4mv[i])
                    '''
                    _key = list(GroupSet[viewGP]['trend']['mv'][i -1].keys())
                    BarArray = [datetime.datetime.fromtimestamp(float(key)) for key in _key
                                if type(GroupSet[viewGP]['trend']['mv'][i -1][key]) != collections.deque]
                    ydata1 = [GroupSet[viewGP]['trend']['mv'][i -1][key] for key in _key
                              if type(GroupSet[viewGP]['trend']['mv'][i -1][key]) != collections.deque]
                    path4mv[i].set_data(BarArray, ydata1)
                    del _key, BarArray, ydata1
                    '''
                    path4trend[i] = Line2D([], [], color = prpd4main[i][0].get_color(), label = _lbl, linewidth = 2)
                    lpath.append(path4trend[i])
                    legend_txt.append(vars(path4trend[i])['_label'])
                    self.ax4trend.add_line(path4trend[i])
                    '''
                    _key = list(GroupSet[viewGP]['trend']['counters'][i -1].keys())
                    BarArray = [datetime.datetime.fromtimestamp(float(key)) for key in _key
                                if type(GroupSet[viewGP]['trend']['mv'][i -1][key]) != collections.deque]
                    ydata1 = [GroupSet[viewGP]['trend']['counters'][i -1][key] for key in _key
                              if type(GroupSet[viewGP]['trend']['mv'][i -1][key]) != collections.deque]
                    path4trend[i].set_data(BarArray, ydata1)
                    del _key, BarArray, ydata1
                    '''
                    pass
                else:
                    lbl = ''
                    pass
                pass
            '''
            path4trend[i] = Line2D([], [], color = prpd4main[i][0].get_color(), label = _lbl, linewidth = 2)
            lpath.append(path4trend[i])
            legend_txt.append(vars(path4trend[i])['_label'])
            self.ax4trend.add_line(path4trend[i])

            path4mv[i] = Line2D([], [], color = prpd4main[i][0].get_color(), label = _lbl, linewidth = 2)
            lpath2.append(path4mv[i])
            self.ax4mv.add_line(path4mv[i])
            '''

        self.def_til_font.set_size(math.ceil(12*72/figDpi))
        self.legend =self.ax4trend.legend(lpath, legend_txt,
                                          prop = self.def_til_font, bbox_to_anchor=(1.15, 1),
                                          loc = 'upper right')
        #self.legend =self.ax4trend.legend(lpath, legend_txt,
                                          #prop = self.def_til_font, loc = 2)
        
        xfmt = matplotlib.dates.DateFormatter('%m/%d\n%H:%M')
        self.ax4trend.xaxis.set_major_formatter(xfmt)
        self.ax4mv.xaxis.set_major_formatter(xfmt)
        self.ax4trend.set_xlim([_xmin, _xmax])
        self.ax4mv.set_xlim([_xmin, _xmax])
        #self.ax4trend.set_ylim(ymin = 0)
        #self.ax4mv.set_ylim(ymin = 0)
        self.ax4trend.set_ylim(bottom = 0)
        self.ax4mv.set_ylim(bottom = 0)
        self.ax4trend.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%d'))
        self.ax4mv.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
        [label.set_fontproperties(self.def_til_font) for label in self.ax4trend.get_yticklabels()]
        [label.set_fontproperties(self.def_til_font) for label in self.ax4mv.get_yticklabels()]
        self.ax4trend.set_xticklabels([])
        [label.set_fontproperties(self.def_til_font) for label in self.ax4mv.get_xticklabels()]
        [label.set_fontproperties(self.def_til_font) for label in self.ax4mv.get_yticklabels()]
        [label.set_fontproperties(self.def_til_font) for label in self.ax4trend.get_yticklabels()]
        self.ax4trend.grid()
        self.ax4mv.grid()
        
        self.ax4trend.set_autoscaley_on(True)
        self.ax4mv.set_autoscaley_on(True)
        
        self.ax4trend.relim()
        self.ax4mv.relim()
        self.ax4trend.autoscale_view()
        self.ax4mv.autoscale_view()
        self.ax4mv.get_shared_x_axes().join(self.ax4mv, self.ax4trend)
        self.ax4trend.callbacks.connect('xlim_changed', self.on_xlims_change)
        self.ax4mv.callbacks.connect('xlim_changed', self.on_xlims_change)
        self.fig4trend.canvas.draw()
        #self.fig4trend.canvas.flush_events()

        pass
    def on_xlims_change(self, event_ax):
        #print("updated xlims: ", time.time(), event_ax, event_ax.get_xlim())
        pass

    def SetTimeInv(self, value):
        pass
#=================================================================
#==================== ChxLblFrm2 =================================
class ChxLblFrm2(tk.LabelFrame):
    def __init__(self, parent, chArry = {}):
        global chk_0_Img,chk_1_Img,curPath,sensors,sensorOption,trivlist
        global AlarmCfg,gainDict,trig_chAry,Config4Lan
        tk.LabelFrame.__init__(self, parent)

        self.parent = parent
        self.chAarry = chArry
        self.icon4triv = Image.open(curPath + "//tvn1Y5s.png")
        self.icon4triv = self.icon4triv.resize((20, 20), Image.ANTIALIAS)
        self.icon4triv = ImageTk.PhotoImage(self.icon4triv)
        self.config(relief = tk.GROOVE, bg = '#ffffff', width = 625, height = 115, bd = 1)
        #print('self.chAarry:', self.chAarry)
        self.config(font = ('IPAGothic', 12, 'bold'))   #群組n
        self.Grx_trigChx = tk.IntVar()
        self.Grx_trigLv = tk.StringVar()
        self.Grx_trigLv.set((list(trivitem.keys())[list(trivitem.values()).index(self.chAarry['trig_lv'])]))
        #print(list(trivitem.values()).index(self.chAarry['trig_lv']))
        #self.trig_ch = [16, 1]
        self.GaintAry = list(gainDict.keys())
        self.gainary = [('00000000' +bin(self.chAarry['gain'])[2:])[-8:][:4],
                        ('00000000' +bin(self.chAarry['gain'])[2:])[-8:][-4:]]

        self._v = bin(self.chAarry['view'])
        #print(self._v)  #0b11
        self._v = self._v[2:].zfill(len(self.chAarry['ch']))
        #print(self._v)  #11
        self._s = hex(self.chAarry['sensor'])
        #print(self._s)  #0x24
        self._s = self._s[2:].zfill(len(self.chAarry['ch']))
        #print(self._s)  #24

        self.view = []
        self.sensor = []
        while ((len(self._v) >0) and (len(self._s) >0)):
            try:
                self.view.append(int(self._v[0], 2))
                self._v = self._v[1:]
                self.sensor.append(int(self._s[0], 16))
                self._s = self._s[1:]
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                break

        #====================== Trigger Lev. setting =======================
        self.GrxTrigLvFrm = tk.Frame(self, relief = tk.FLAT, bg = self['bg'])
        self.GrxTrigLvOpt = tk.Button(self.GrxTrigLvFrm, text = '', font = ('IPAGothic', 13, 'normal'),
                                      relief = tk.RAISED, bd = 2,
                                      compound="left", image = self.icon4triv)
        #'GrxTrigLvOpt = IENHHHLFNHGGIGDEJHAEPHLH'
        self.GrxTrigLvOpt.config(text = Config4Lan.get(AlarmCfg['lang'], 'IENHHHLFNHGGIGDEJHAEPHLH'))
        '''
        self.GrxTrigLvOpt.config(text = {
            'zh-TW' : lambda : '局放位準',
            'en-US' : lambda : 'PD. Level',
            }.get(AlarmCfg['lang'], lambda : '局放位準')())
        '''
        self.GrxTrigLvOpt.config(command = lambda para = self.Grx_trigLv: self.actTrivFrm(para))

        self.GrxTrigLvLbl = tk.Label(self.GrxTrigLvFrm)
        self.GrxTrigLvLbl.config(textvariable = self.Grx_trigLv,
                                    font = ('IPAGothic', 16, 'normal'), underline = 0)
        self.GrxTrigLvLbl.config(bg = self['bg'], relief = tk.RAISED, bd = 2)

        self.GrxTrigLvOpt.place(x = 0, y = 0, height = 40, width = 110)
        self.GrxTrigLvLbl.place(x = 110, y = 0, height = 40, width = 40)
        self.GrxTrigLvFrm.place(x = 465, y = 0, height = 40, width = 155)
        #===================================================================

        _i = 0
        for i in self.chAarry['ch']:
            vars(self)[('Ch_%s' %_i)] = i
            vars(parent)[('Ch%s_var' %i)] = tk.IntVar()
            vars(parent)[('Ch%s_sensor_variable' %i)] = tk.StringVar()
            vars(parent)[('Ch%s_TrigLev_variable' %i)] = tk.StringVar()

            #========================= Ch X Label ===============================
            
            vars(self)[('Ch%s_Lbl' %i)] = tk.Label(self, bg = self['bg'],
                                                   text = '%s %s' %(Config4Lan.get(AlarmCfg['lang'], 'channel'), i),
                                                   #text = {
                                                       #'zh-TW' : lambda : ("通道 %s" %i),
                                                       #'en-US' : lambda : ("Ch %s" %i),
                                                       #}.get(AlarmCfg['lang'], lambda : ("通道 %s" %i))(),
                                                   relief = tk.FLAT, bd = 0,
                                                   font = ('IPAGothic', 8, 'normal'),
                                                   wraplength = 1,
                                                   compound="center")

            #========================= Ch X view ===============================
            #vars(parent)[('Ch%s_var' %i)].set(globals()[('ch%s_view' %i)])
            vars(parent)[('Ch%s_var' %i)].set(self.view[_i])
            vars(parent)[('Ch%s_View' %i)] = tk.Label(self, bd = 0, relief = tk.FLAT,
                                                            image = chk_1_Img)
            '''
            vars(parent)[('Ch%s_View' %i)] = tk.Checkbutton(self, variable = vars(parent)[('Ch%s_var' %i)],
                                                            bd = 0, relief = tk.FLAT,
                                                            image = chk_0_Img,
                                                            selectimage = chk_1_Img)
            vars(parent)[('Ch%s_View' %i)].config(activebackground = "#ffffff", bg = self['bg'], indicatoron  = 0, onvalue = 1)
            vars(parent)[('Ch%s_View' %i)].config(offvalue = 0, compound = tk.LEFT)
            vars(parent)[('Ch%s_View' %i)].config(command = lambda ch = i: parent.SetCh_View(ch))
            '''
            #===================================================================
            #======================== Ch X sensor ==============================
            #vars(parent)[('Ch%s_sensorImg' %i)] = Image.open((curPath + "//" + sensors[sensorOption[globals()[('ch%s_sensor' %i)]]][1]))
            vars(parent)[('Ch%s_sensorImg' %i)] = Image.open((curPath + "//" + sensors[sensorOption[self.sensor[_i]]][1]))
            vars(parent)[('Ch%s_sensorImg' %i)] = vars(parent)[('Ch%s_sensorImg' %i)].resize((35, 35), Image.ANTIALIAS)
            vars(parent)[('Ch%s_sensorImg' %i)] = ImageTk.PhotoImage(vars(parent)[('Ch%s_sensorImg' %i)])
            vars(parent)[('Ch%s_sensorPic' %i)] = tk.Label(self, bg = self['bg'], compound="center")
            vars(parent)[('Ch%s_sensorPic' %i)].config(image = vars(parent)[('Ch%s_sensorImg' %i)])
            
            #vars(parent)[('Ch%s_sensor_variable' %i)].set(sensorOption[globals()[('ch%s_sensor' %i)]])
            vars(parent)[('Ch%s_sensor_variable' %i)].set(sensorOption[self.sensor[_i]])
            vars(parent)[('Ch%s_sensor' %i)] = tk.OptionMenu(self, vars(parent)[('Ch%s_sensor_variable' %i)], '')

            vars(parent)[('Ch%s_sensor' %i)].config(font = ('IPAGothic', 13, 'normal'))
            vars(parent)[('Ch%s_sensor' %i)]['menu'].config(font = ('IPAGothic',13, 'normal'))
            vars(parent)[('Ch%s_sensor' %i)]['menu'].delete(0, 'end')
            [vars(parent)[('Ch%s_sensor' %i)]['menu'].add_command(
                label = item,
                command = lambda value = (i, item): self.SetCh_Sensor(value))
             for item in sensorOption]
            #===================================================================
            #========================= Ch X Gain ===============================
            self.ChxGainLbl = tk.Label(self, bg = self['bg'], compound="center",
                                       font = ('IPAGothic', 14, 'normal'),
                                       text =  'Gain')

            '''
            vars(parent)[('Ch%s_gain_variable' %i)] = tk.IntVar()
            self.GaintAry = (1, 10, 20, 30)
            self.xGainLbl = tk.Label(self, bg = self['bg'], compound="center",
                                     font = ('IPAGothic', 16, 'bold'),
                                     text =  'X')
            vars(parent)[('Ch%s_gain' %i)].place(x = 330, y = (_i *50), height = 45, width = 60)
            self.xGainLbl.place(x = 390, y = (_i *50) +15, height = 25, width = 15)
            '''
            vars(parent)[('Ch%s_gain_variable' %i)] = tk.StringVar()
            #self.GaintAry = ('1.0x', '2.0x', '3.5x', '8.5x')
            #print(self.gainary[_i])
            try:
                _gain = [key for key in gainDict if gainDict[key][_i] == self.gainary[_i]][0]
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                _gain = '10x'
            vars(parent)[('Ch%s_gain_variable' %i)].set(_gain)
            
            vars(parent)[('Ch%s_gain' %i)] = tk.OptionMenu(self, vars(parent)[('Ch%s_gain_variable' %i)],
                                                             *self.GaintAry)#,
                                                             #command = self.SetCh_Sensor)
            
            vars(parent)[('Ch%s_gain' %i)].config(font = ('IPAGothic', 16, 'normal'))
            vars(parent)[('Ch%s_gain' %i)]['menu'].config(font = ('IPAGothic',13, 'normal'))
            #===================================================================
            #======================= Trigger Ch select =========================
            
            self.Grx_trigChx.set(self.chAarry['trig_ch'])
            vars(parent)[('Ch%s_trig' %i)] = tk.Radiobutton(self, text = '',
                                                            bd = 0,
                                                            bg = self['bg'],
                                                            indicatoron = 0,
                                                            image = chk_0_Img,
                                                            selectimage = chk_1_Img,
                                                            variable = self.Grx_trigChx,
                                                            #value = self.trig_ch[_i],
                                                            value = trig_chAry[_i],
                                                            command = self.TrigSet)
            
            #===================================================================
            #====================== Trigger Lev. setting =======================
            '''
            vars(parent)[('Ch%s_TrigLevOpt' %i)] = tk.Button(self, text = '', font = ('IPAGothic', 13, 'bold'),
                                                             relief = tk.RAISED, bd = 2,
                                                             compound="left", image = self.icon4triv)

            vars(parent)[('Ch%s_TrigLevOpt' %i)].config(text = {
                'zh-TW' : lambda : '局放位準',
                'en-US' : lambda : 'PD. Level',
                }.get(lang, lambda : '局放位準')())

            vars(parent)[('Ch%s_TrigLev_variable' %i)].set((list(trivitem.keys())[list(trivitem.values()).index(float(globals()[('ch%s_triv' %i)]))]))
            vars(parent)[('Ch%s_TrigLevOpt' %i)].config(command = lambda para = [vars(parent)[('Ch%s_TrigLev_variable' %i)], i]: parent.actTrivFrm(para))

            vars(parent)[('Ch%s_TrigLevLbl' %i)] = tk.Label(self)
            vars(parent)[('Ch%s_TrigLevLbl' %i)].config(textvariable = vars(parent)[('Ch%s_TrigLev_variable' %i)],
                                                        font = ('IPAGothic', 16, 'bold'), underline = 0)
            vars(parent)[('Ch%s_TrigLevLbl' %i)].config(bg = self['bg'], relief = tk.RAISED, bd = 2)
            vars(parent)[('Ch%s_TrigLevOpt' %i)].place(x = 470, y = (_i *50), height = 45, width = 110)
            vars(parent)[('Ch%s_TrigLevLbl' %i)].place(x = 580, y = (_i *50), height = 45, width = 40)
            '''
            #===================================================================

            vars(self)[('Ch%s_Lbl' %i)].place(x = 0, y = (_i *45))
            vars(parent)[('Ch%s_View' %i)].place(x = 15, y = (_i *45))
            vars(parent)[('Ch%s_sensorPic' %i)].place(x = 60, y = (_i *45))
            vars(parent)[('Ch%s_sensor' %i)].place(x = 110, y = (_i *45), height = 40, width = 170)
            self.ChxGainLbl.place(x = 285, y = (_i *42), height = 40, width = 50)
            vars(parent)[('Ch%s_gain' %i)].place(x = 335, y = (_i *45), height = 40, width = 80)
            vars(parent)[('Ch%s_trig' %i)].place(x = 420, y = (_i *45))
            vars(self)[('Ch%s_Lbl' %i)].tkraise()
            _i = _i +1

    def actTrivFrm(self, para):
        global root,trig_chAry
        var = para
        #_y = [ _y for _y in range(0, len(self.trig_ch)) if self.trig_ch[_y] == self.Grx_trigChx.get()][0]
        _y = [ _y for _y in range(0, len(trig_chAry)) if trig_chAry[_y] == self.Grx_trigChx.get()][0]
        ch = self.chAarry['ch'][_y]

        UpdateOptStates(tilBar, 0)
        UpdateOptStates(StatusBar, 0)
        UpdateOptStates(self, 0)
        thisFrm = tilBar.control_variable.get()
        lKey = [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if thisFrm in x][0])][0]
        UpdateOptStates(Opt2ActFrm[lKey][2], 0)

        args = [self, var, ch,]
        VisualNumPad = CreateVisualKeyboard('TrivForm', 'VisualNumPad', args)
        VisualNumPad.focus_set()

    def TrigSet(self):
        global trig_chAry
        #_y = [ _y for _y in range(0, len(self.trig_ch)) if self.trig_ch[_y] == self.Grx_trigChx.get()][0]
        _y = [ _y for _y in range(0, len(trig_chAry)) if trig_chAry[_y] == self.Grx_trigChx.get()][0]
        self.GrxTrigLvFrm.place(x = 465, y = (_y *50), height = 45, width = 155)
        '''
        for i in range(0, len(self.trig_ch)):
            if self.trig_ch[i] != self.Grx_trigChx.get():
                vars(self.parent)[('Ch%s_TrigLevOpt' %self.chAarry['ch'][i])].config(state = LawStatus[0])
                pass
            else:
                vars(self.parent)[('Ch%s_TrigLevOpt' %self.chAarry['ch'][i])].config(state = LawStatus[1])
                pass
        '''
        pass

    def SetCh_Sensor(self, value):
        global curPath,sensors,sensorOption
        s1 = sensors[value[1]][0]
        vars(self.parent)[('Ch%s_sensor_variable' %value[0])].set(value[1])
        vars(self.parent)[('Ch%s_sensorImg' %value[0])] = Image.open((curPath + "//" + sensors[sensorOption[s1]][1]))
        vars(self.parent)[('Ch%s_sensorImg' %value[0])] = vars(self.parent)[('Ch%s_sensorImg' %value[0])].resize((40, 40), Image.ANTIALIAS)
        vars(self.parent)[('Ch%s_sensorImg' %value[0])] = ImageTk.PhotoImage(vars(self.parent)[('Ch%s_sensorImg' %value[0])])
        vars(self.parent)[('Ch%s_sensorPic' %value[0])].config(image = vars(self.parent)[('Ch%s_sensorImg' %value[0])])
#=============================================================
#======================= Triv Windows =========================
class TrivForm(tk.Toplevel):
    def __init__(self, parent, var, ch):
        global curPath,AlarmCfg,trivlist,icon4Save,loginlaw
        tk.Toplevel.__init__(self, parent)
        self.icon = tk.PhotoImage( file = (curPath +"//tvn1Y5s.png"))
        #self.resizable(width = False, height = False)    #可否變更大小
        
        self.parent = parent
        self.var = var
        self.ch = ch
        self.lblvariable = tk.StringVar()
        #'TrivForm_til = LFNHGGJHJEAGNHCGAFLHGGDG
        self.lblvariable.set(Config4Lan.get(AlarmCfg['lang'], 'LFNHGGJHJEAGNHCGAFLHGGDG', vars={'para1': self.ch}))
        '''
        self.lblvariable.set(
            {
                'zh-TW' : lambda : ("請設定 通道%s 局放位準" %self.ch),
                'en-US' : lambda : ("Setting Ch%s Trigger Lev" %self.ch),
                }.get(AlarmCfg['lang'], lambda : ("請設定 通道%s 局放位準" %self.ch))()
            )
        '''
        self.title(self.lblvariable.get())
        self.tk.call('wm', 'iconphoto', self._w, self.icon)
        self.configure(background='#ffffff', takefocus = True, bd = 5)    #背景顏色
        #================== 視窗大小及置中 =================
        wnWidth = self.winfo_screenwidth()
        wnHeight = self.winfo_screenheight()
        w ,h = 520, 200
        size = (w ,h)
        left = (wnWidth - w) /2
        top = (wnHeight - h) /2
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))
        #===================================================
        self.resizable(width = False, height = False)    #可否變更大小
        self.attributes("-topmost", 1) #最上層顯示
        self.protocol("WM_DELETE_WINDOW", self.on_exit)    #重新導向 Close Even
        self.transient(self.parent)
        self.bind("<Unmap>", self.on_exit2)
        #self.bind('<FocusOut>', self.on_exit)
        #self.grab_set()
        #self.attributes("-toolwindow", 1)

        loginlaw = GetGlobals('loginlaw')

        self.name = None
        self.strUnmap = []
        self.tmpUnmap = None
        self.numUnmap = 0
        self._job =None

        if loginlaw >= 2:
            _initTrig = 0
        else:
            _initTrig = 1

        tk.Label(self, textvariable = self.lblvariable,
                 relief = tk.FLAT, bd = 0,
                 font = ('IPAGothic', 24, 'normal'),
                 fg = '#0000ff', bg = '#ffffff'
                 ).grid(column = 0, row = 0)
        self.trigscale = tk.Scale(self, from_ = _initTrig,#1,
                                  to = (len(trivlist) -1), bg = '#ffffff',
                                  font = ('IPAGothic', 24, 'bold'),
                                  width = 60, sliderlength = 60,
                                  length = 500, orient = tk.HORIZONTAL )
        self.trigscale.grid(column = 0, row = 1)

        self.trigscale.set(self.var.get())

    def on_exit(self, *args):
        global tilBar,StatusBar
        
        self.var.set(str(self.trigscale.get()))

        #self.destroy()
        #UpdateOptStates(tilBar, 1)
        #UpdateOptStates(StatusBar, 1)
        #thisFrm = tilBar.control_variable.get()
        #lKey = [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if thisFrm in x][0])][0]
        #UpdateOptStates(Opt2ActFrm[lKey][2], 1)
        #PopGlobals(self.name)

        try:
            #GetGlobals(self.name).destroy()
            UpdateOptStates(tilBar, 1)
            UpdateOptStates(StatusBar, 1)
            thisFrm = tilBar.control_variable.get()
            lKey = [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if thisFrm in x][0])][0]
            UpdateOptStates(Opt2ActFrm[lKey][2], 1)
            PopGlobals(self.name)
            self.destroy()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
        pass

    def on_exit2(self, *args):
        self.strUnmap.append(time.time())
        if self._job is None:
            self._job = self.after(100, self.update_clock)

    def update_clock(self):
        global root
        root.deiconify()
        root.focus_set()
        if self.tmpUnmap == max(self.strUnmap):
            self.numUnmap = self.numUnmap +1
            if self.numUnmap >=2:
                if self._job is not None:
                    self.after_cancel(self._job)
                    self._job = None
                self.on_exit()
                pass
        else:
            self.tmpUnmap = max(self.strUnmap)
            self.numUnmap = 0

        self._job = self.after(100, self.update_clock)
        
#========================= Alarm Frame2 ==========================
class AlarmFrm2(tk.Frame):
    def __init__(self, parent, controller, law):
        global tilBar,StatusBar,AlarmCfg,Config4Lan
        global LawStatus#,loginlaw
        #global FFilter_variable        
        tk.Frame.__init__(self,parent)
        h = parent['height'] -tilBar['height'] -StatusBar['height'] #H = 374

        self.config(relief = tk.GROOVE, bg = '#ffffff', width = parent['width'] -40, height = h)
        self.place(x = 0, y = tilBar['height'])
        self.law = law

        #self.chs = {1: '１', 2: '２', 3: '３', 4: '４', 5: '５', 6: '６'}
        #self.chs = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六'}
        #self.chc = {1: "#ff9600", 2: "#ff0000", 3: "#0000FF", 4: "#00ff00", 5: '#FF1493', 6: '#4B0082'}
        
        for j in GroupSet:
            vars(self)[('Gr%s_Conf' %j)] = ChxLblFrm2(self, GroupSet[j])
            vars(self)[('Gr%s_Conf' %j)].config(text = '%s%s' %(Config4Lan.get(AlarmCfg['lang'], 'group'), j))
            '''
            vars(self)[('Gr%s_Conf' %j)].config(text = {
                'zh-TW' : lambda : ("群組%s" %j),
                'en-US' : lambda : ("Group %s" %j),
                }.get(AlarmCfg['lang'], lambda : ("群組%s" %j))())
            '''
            vars(self)[('Gr%s_Conf' %j)].place(x = 5, y = ((j*115) +5))
            vars(self)[('Gr%s_Conf' %j)].TrigSet()
        '''
        Alarm_type = tk.LabelFrame(self, relief = tk.GROOVE, bg = '#ffffff',
                                   width = 135, height = 160, bd = 1)

        Alarm_type.config(text = ({
            'zh-TW' : lambda : "警示類型",
            'en-US' : lambda : "Alarm Type",
            }.get(lang, lambda : "警示類型")()),
                          font = ('IPAGothic', 13, 'bold'),
                          fg = "#000000")
        #Alarm_type.place(x = 625, y = 5)

        arString = bin(alarm_type)
        arString = arString[2:]
        arString = '000' + arString
        arString = arString[-3:]
        isEm = int(arString[2:3])
        isBe = int(arString[1:2])
        isLi = int(arString[0:1])

        self.Alarm_mail_var = tk.IntVar()
        self.Alarm_mail_var.set(isEm)
        Alarm_mail = tk.Checkbutton(Alarm_type, variable = self.Alarm_mail_var,
                                    bd = 0, relief = tk.FLAT, image = chk_0_Img,
                                    selectimage = chk_1_Img, onvalue = 1,
                                    offvalue = 0, command = lambda ch = 0: self.SetAlarm_Type(ch))
        Alarm_mail.config(activebackground = "#ffffff",bg = "#ffffff", indicatoron  = 0)
        Alarm_mail.config(offvalue = 0, compound = tk.LEFT, state = tk.DISABLED)
        Alarm_mail_variable = tk.StringVar()
        Alarm_mail_variable.set(
            {
                'zh-TW' : lambda : '電子郵件',
                'en-US' : lambda : 'Email',
                }.get(lang, lambda : '電子郵件')())
        Alarm_mail.config(textvariable = Alarm_mail_variable, font = ('IPAGothic', 13, 'bold'))

        self.Alarm_bee_var = tk.IntVar()
        self.Alarm_bee_var.set(isBe)
        Alarm_bee = tk.Checkbutton(Alarm_type, variable = self.Alarm_bee_var,
                                   bd = 0, relief = tk.FLAT, image = chk_0_Img,
                                   selectimage = chk_1_Img, onvalue = 1,
                                   offvalue = 0, command = lambda ch = 1: self.SetAlarm_Type(ch))
        Alarm_bee.config(activebackground = "#ffffff",bg = "#ffffff", indicatoron  = 0)
        Alarm_bee.config(offvalue = 0, compound = tk.LEFT, state = tk.NORMAL)
        Alarm_bee_variable = tk.StringVar()
        Alarm_bee_variable.set(
            {
                'zh-TW' : lambda : '蜂  鳴  器',
                'en-US' : lambda : 'Buzzer',
                }.get(lang, lambda : '蜂  鳴  器')())
        Alarm_bee.config(textvariable = Alarm_bee_variable, font = ('IPAGothic', 13, 'bold'))

        self.Alarm_light_var = tk.IntVar()
        self.Alarm_light_var.set(isLi)
        Alarm_light = tk.Checkbutton(Alarm_type, variable = self.Alarm_light_var,
                                     bd = 0, relief = tk.FLAT, image = chk_0_Img,
                                     selectimage = chk_1_Img, onvalue = 1,
                                     offvalue = 0, command = lambda ch = 2: self.SetAlarm_Type(ch))
        Alarm_light.config(activebackground = "#ffffff",bg = "#ffffff", indicatoron  = 0)
        Alarm_light.config(offvalue = 0, compound = tk.LEFT, state = tk.NORMAL)
        Alarm_light_variable = tk.StringVar()
        Alarm_light_variable.set(
            {
                'zh-TW' : lambda : '警  示  燈',
                'en-US' : lambda : 'Light',
                }.get(lang, lambda : '警  示  燈')())
        Alarm_light.config(textvariable = Alarm_light_variable, font = ('IPAGothic', 13, 'bold'))

        Alarm_mail.place(x = 5, y = 5)
        Alarm_bee.place(x = 5, y = 45)
        Alarm_light.place(x = 5, y = 85)
        '''
        '''
        Reffreq_Conf = tk.LabelFrame(self, relief = tk.GROOVE, bg = '#ffffff', width = 125, height = 70, bd = 1)
        Reffreq_Conf.config(text = {
            'zh-TW' : lambda : "工作頻率",
            'en-US' : lambda : "Sync Freq.",
            }.get(lang, lambda : "工作頻率")())
        Reffreq_Conf.config(font = ('IPAGothic', 13, 'bold'), fg = "#000000")
        Reffreq_Conf.place(x = self['width'] -125, y = 5)
        ReffreqLbl = tk.Label(Reffreq_Conf, text = "Hz", font = ('IPAGothic', 13, 'bold'), bg = "#ffffff")
        ReffreqLbl.place( x = 90, y = 15)

        self.ReffreqScale = (50.0, 60.0)
        self.Reffreq_variable = tk.DoubleVar()
        self.Reffreq_variable.set(reffreq)
        ReffreqOpt = tk.OptionMenu(Reffreq_Conf, self.Reffreq_variable, *self.ReffreqScale, command = self.SetReffreq)
        ReffreqOpt['menu'].config(font = ('IPAGothic',13, 'bold'))
        ReffreqOpt.config(font = ('IPAGothic', 13, 'bold'), width = 4, height = 1)
        ReffreqOpt.place(x = 5, y = 5)
        '''

        self.PDTimes_variable = tk.IntVar()
        PDTimes_Conf = tk.LabelFrame(self, relief = tk.GROOVE, bg = '#ffffff', width = 125, height = 70, bd = 1)
        PDTimes_Conf.config(text = Config4Lan.get(AlarmCfg['lang'], 'MEOGDGMGKHJENHCGAFMHKHCGLHHHLH'))
        '''
        PDTimes_Conf.config(text = {
            'zh-TW' : lambda : "放電次數",
            'en-US' : lambda : "Counters",
            }.get(AlarmCfg['lang'], lambda : "放電次數")())
        '''
        PDTimes_Conf.config(font = ('IPAGothic', 13, 'bold'), fg = "#000000")
        PDTimes_Conf.place(x = self['width'] -125, y = 5)
        PDTimesOutfrm = tk.LabelFrame(PDTimes_Conf, relief = tk.FLAT, bg = '#ffffff', width = 115, height = 35, bd = 1)
        PDTimesOutfrm.place(x = 5, y = 5)
        self.PDTimesOpt = tk.Entry(PDTimesOutfrm, bd = 2, textvariable = self.PDTimes_variable,
                                   font = ('IPAGothic', 13, 'normal'),width = 6)
        self.PDTimes_variable.set(AlarmCfg['maxpoint'])
        self.PDTimesOpt.place(x = 0, y = 0, height = 35)
        #'NumPad4PDTimes_txt = BEKHCGPFOGLGLDPFLELFGGCGKGMHAFLHHHLH'
        txt = Config4Lan.get(AlarmCfg['lang'], 'BEKHCGPFOGLGLDPFLELFGGCGKGMHAFLHHHLH')
        '''
        txt = (
            {
                'zh-TW' : lambda : '請輸入放電次數：',
                'en-US' : lambda : 'Enter Counters：',
                }.get(AlarmCfg['lang'], lambda : '請輸入放電次數：')())
        '''
        NumPad4PDTimes = tk.Button(PDTimesOutfrm, text='', image = numpadicon, compound="center",
                                   command = lambda para = [self.PDTimes_variable, txt]: self.actNumPad(para))
        NumPad4PDTimes.place(x = 80, y = 0)
        PDTimesLbl_variable = tk.StringVar()
        '''
        PDTimesLbl_variable.set(
            {
                'zh-TW' : lambda : '次',
                'en-US' : lambda : '',
                }.get(AlarmCfg['lang'], lambda : '次')())
        '''
        PDTimesLbl = tk.Label(PDTimes_Conf, textvariable = PDTimesLbl_variable,
                              font = ('IPAGothic', 13, 'bold'), bg = "#ffffff")
        PDTimesLbl.place( x = 75, y = 10)

        self.PDDurat_variable = tk.IntVar()
        PDDurat_Conf = tk.LabelFrame(self, relief = tk.GROOVE, bg = '#ffffff', width = 125, height = 70, bd = 1)
        PDDurat_Conf.config(text = Config4Lan.get(AlarmCfg['lang'], 'MEOGDGMGKHJENHCGAFLGKHNHLHHHLH'))
        '''
        PDDurat_Conf.config(text = {
            'zh-TW' : lambda : '持續時間',
            'en-US' : lambda : 'Duration',
            }.get(AlarmCfg['lang'], lambda : '持續時間')())
        '''
        PDDurat_Conf.config(font = ('IPAGothic', 13, 'bold'), fg = "#000000")
        PDDurat_Conf.place(x = self['width'] -125, y = 75)
        PDDuratOutfrm = tk.LabelFrame(PDDurat_Conf, relief = tk.FLAT, bg = '#ffffff', width = 115, height = 35, bd = 1)
        PDDuratOutfrm.place(x = 5, y = 5)
        self.PDDuratOpt = tk.Entry(PDDuratOutfrm, bd = 2, textvariable = self.PDDurat_variable,
                                   font = ('IPAGothic', 13, 'normal'), width = 6)
        self.PDDurat_variable.set(AlarmCfg['maxdurat'])
        self.PDDuratOpt.place(x = 0, y = 0, height = 35)
        #'NumPad4PDDurat_txt = BEKHCGPFOGLGLDPFLELEKHNHOGLHAFLHHHLH'
        txt = Config4Lan.get(AlarmCfg['lang'], 'BEKHCGPFOGLGLDPFLELEKHNHOGLHAFLHHHLH')
        '''
        txt = (
            {
                'zh-TW' : lambda : '請輸入持續時間：',
                'en-US' : lambda : 'Enter Duration：',
                }.get(AlarmCfg['lang'], lambda : '請輸入持續時間：')())
        '''
        NumPad4PDDurat = tk.Button(PDDuratOutfrm, text='', image = numpadicon,
                                   compound="center",
                                   command = lambda para = [self.PDDurat_variable, txt]: self.actNumPad(para))
        NumPad4PDDurat.place(x = 80, y = 0)
        PDDuratLbl_variable = tk.StringVar()
        '''
        PDDuratLbl_variable.set(
            {
                'zh-TW' : lambda : '秒',
                'en-US' : lambda : 'S.',
                }.get(AlarmCfg['lang'], lambda : '秒')())
        '''
        PDDuratLbl = tk.Label(PDDurat_Conf, textvariable = PDDuratLbl_variable,
                              font = ('IPAGothic', 13, 'bold'), bg = "#ffffff", fg = "#ff0000")
        PDDuratLbl.place( x = 75, y = 10)

        '''
        self.isfilter_var = tk.IntVar()
        self.isfilter_var.set(AlarmCfg['isfilter'])
        self.isfilter = tk.Checkbutton(self, variable = self.isfilter_var,
                                       bd = 0, relief = tk.FLAT, image = chk_0_Img,
                                       selectimage = chk_1_Img, onvalue = 1,
                                       offvalue = 0)
        self.isfilter.config(activebackground = "#ffffff",bg = "#ffffff", indicatoron  = 0)
        self.isfilter.config(compound = tk.LEFT, state = tk.NORMAL)

        self.isfilter.config(text = {
            'zh-TW' : lambda : 'High Pass',
            'en-US' : lambda : 'High Pass',
            }.get(AlarmCfg['lang'], lambda : 'High Pass')(),
                             font = ('IPAGothic', 13, 'bold'))
        self.isfilter.place(x = self['width'] -125, y = 145)
        '''

        Save4AlarmBtn = tk.Button(self, text='', font = ('IPAGothic', 13, 'bold'), image = icon4Save,
                                  compound="center", command = self.Save4Alarm)
        Save4AlarmBtn.config(activebackground = "#ffffff", bg = '#ffffff', relief = tk.FLAT, bd = 0)
        Save4AlarmBtn.place(x = self['width'] -125, y = self['height'] -65)
        '''
        i = 0
        for j in GroupSet:  #載入觸發通道TrivLev
            for k in range(0, (len(GroupSet[j]['ch']))):
                i = i+1
                self.SetTrigLev(vars(self)[('Ch%s_TrigLev_variable' %i)].get(), vars(vars(self)[('Ch%s_Conf' %i)])['Chx'])
                self.SetCh_View(vars(vars(self)[('Ch%s_Conf' %i)])['Chx'])
        del arString,isEm,isBe,isLi
        '''
        if self.law >0:
            loginlaw = GetGlobals('loginlaw')
            UpdateOptStates(self, int(self.law <= loginlaw))
    '''
    def SetTrigLev(self, value, ch):
        global thisOS,trivitem,ch1_triv,ch2_triv,ch3_triv,ch4_triv
        #print(value, ch)
        setVol = trivitem[value]
        if ch == 1:
            ch1_triv = setVol
        elif ch == 2:
            ch2_triv = setVol
        elif ch == 3:
            ch3_triv = setVol
        elif ch == 4:
            ch4_triv = setVol
        else:
            pass

        chip = (math.ceil(ch /2) -1)
        #ch = ("%1s" % (math.floor(((ch%2)+1)%2)))
        ch = ("%1s" % (math.floor(ch%2)))
        ''''''
        chip || ch || Channel
          0  || 1  ||   1
          0  || 0  ||   2
          1  || 1  ||   3
          1  || 0  ||   4
        ''''''

                
        if thisOS == 'Windows' :
            commLine = ('python ' + curPath + '//setDACVol.py' + (' %1d' %chip) +
                        (' %1s' % ch) + (' %.1f' %setVol))
        elif thisOS == 'Linux' :
            commLine = ('sudo python3 ' + curPath + '//setDACVol.py' + (' %1d' %chip) +
                        (' %1s' % ch) + (' %.1f' %setVol))
            
        p = subprocess.Popen(commLine, shell = True, stdout = subprocess.PIPE)
        print(p.communicate()[0].decode('ascii'))

        #self.setDAC(int(ch), setVol)
    ''''''
    def setDAC(self, ch, setVol):
        chip = (math.ceil(ch /2) -1)
        setVol = int(math.ceil(setVol / 8))
        bitString = bin(setVol)
        bitString = bitString[2:]
        bitString = '00000000' + bitString
        bitString = bitString[-8:]
        bitString = ("%1s" % (math.floor(((ch%2)+1)%2))) + '011' + bitString + '0000'
        numItem = bitString[:8]
        comItem = bitString[-8:]
        if thisOS == 'Windows' :
            commLine = ('python ' + curPath + '//setDAC.py ' + numItem +
                        ' ' + comItem + ' ' + ('%1d' % chip))
        elif thisOS == 'Linux' :
            commLine = ('sudo python ' + curPath + '//setDAC.py ' + numItem +
                        ' ' + comItem + ' ' + ('%1d' % chip))

        p = subprocess.Popen(commLine, shell = True, stdout = subprocess.PIPE)
        print(p.communicate()[0].decode('ascii'))
    '''
    def SetCh_View(self, ch):
        global AlarmCfg,LawStatus,chx_sel#,loginlaw
        global GroupSet,trig_chAry,showerrorFrm
        err = 0

        for j in GroupSet:
            for k in GroupSet[j]['ch']:
                err = err + vars(self)[('Ch%s_var' %k)].get()

        #'SetCh_View_til = MFKGLHMEHGAFJFGGKGIHAFLHGGDG'
        #'SetCh_View_txt = MFKGLHMEHGAFJFGGKGIHAFLHHHLH'
        if err <= 0:
            til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MFKGLHMEHGAFJFGGKGIHAFLHGGDG'),
                        Config4Lan.get(AlarmCfg['lang'], 'MFKGLHMEHGAFJFGGKGIHAFLHHHLH'))
            '''
            til, txt = (
                {
                    'zh-TW' : lambda : ("訊息", "注意！請至少\n選擇一通道監測"),
                    'en-US' : lambda : ("Information", "Note！Please select at \nleast one channel"),
                    }.get(AlarmCfg['lang'], lambda : ("訊息", "注意！請至少\n選擇一通道監測"))())
            '''
            #tkmsgbox.showerror(til, txt, parent = self)
            '''
            args = [root, til, txt]
            VisualNumPad = CreateVisualKeyboard('showerror', 'VisualNumPad', args)
            VisualNumPad.focus_set()
            self.wait_window(VisualNumPad)
            '''
            showerrorFrm = GetGlobals('showerrorFrm')
            showerrorFrm.msg_var.set(txt)
            showerrorFrm.updatepos('err')
            showerrorFrm.tkraise()
            vars(self)[('Ch%s_var' %ch)].set(1)

        else:
            loginlaw = GetGlobals('loginlaw')
            vars(self)['Ch%s_sensor' %ch].config(state = LawStatus[(vars(self)['Ch%s_var' %ch].get() *loginlaw)])
            #vars(self)['Ch%s_TrigLevOpt' %ch].config(state = LawStatus[(vars(self)['Ch%s_var' %ch].get() *loginlaw)])
            vars(self)[('Ch%s_gain' %ch)].config(state = LawStatus[(vars(self)['Ch%s_var' %ch].get() *loginlaw)])
            vars(self)[('Ch%s_trig' %ch)].config(state = LawStatus[(vars(self)['Ch%s_var' %ch].get() *loginlaw)])
            var = vars(self)['Ch%s_sensor' %ch].cget("state")

            if vars(self)[('Ch%s_var' %ch)].get() == 0:
                _i = [j for j in GroupSet if ch in GroupSet[j]['ch']][0]
                _c = [j for j in range(0, len(GroupSet[_i]['ch'])) if GroupSet[_i]['ch'][j] is not ch][0]
                if vars(self)[('Ch%s_var' %GroupSet[_i]['ch'][_c])].get() == 1:
                    #_t = vars(self)[('Gr%s_Conf' %_i)].trig_ch[_c]
                    _t = trig_chAry[_c]
                    vars(self)[('Gr%s_Conf' %_i)].Grx_trigChx.set(_t)
                    vars(self)[('Gr%s_Conf' %_i)].TrigSet()


    def SetReffreq(self, value):
        pass

    def SetAlarm_Type(self, ch):
        global AlarmCfg,showerrorFrm
        err = self.Alarm_light_var.get() + self.Alarm_bee_var.get() + self.Alarm_mail_var.get()
        if err <= 0:
            #'SetAlarm_Type_til = MFKGLHOEDGOGNHCGAFLFGHPHKGAFLHGGDG'
            #'SetAlarm_Type_txt = MFKGLHOEDGOGNHCGAFLFGHPHKGAFLHHHLH'
            til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MFKGLHOEDGOGNHCGAFLFGHPHKGAFLHGGDG'),
                        Config4Lan.get(AlarmCfg['lang'], 'MFKGLHOEDGOGNHCGAFLFGHPHKGAFLHHHLH'))
            '''
            til, txt = (
                {
                    'zh-TW' : lambda : ("訊息", "注意！請至少\n選擇一種警示類型"),
                    'en-US' : lambda : ("Information", "Note！Please select at\nleast one type of alarm"),
                    }.get(AlarmCfg['lang'], lambda : ("訊息", "注意！請至少\n選擇一種警示類型"))())
            '''
            #tkmsgbox.showerror(til, txt, parent = self)
            '''
            args = [root, til, txt]
            VisualNumPad = CreateVisualKeyboard('showerror', 'VisualNumPad', args)
            VisualNumPad.focus_set()
            self.wait_window(VisualNumPad)
            '''
            showerrorFrm = GetGlobals('showerrorFrm')
            showerrorFrm.msg_var.set(txt)
            showerrorFrm.updatepos('err')
            showerrorFrm.tkraise()
            if ch == 0:
                self.Alarm_mail_var.set(1)
            elif ch == 1:
                self.Alarm_bee_var.set(1)
            elif ch == 2:
                self.Alarm_light_var.set(1)

        #arString = "%1d" %self.Alarm_light_var.get() + "%1d" %self.Alarm_bee_var.get() + "%1d" %self.Alarm_mail_var.get()
        #alarm_type = int(arString,2)


    def Save4Alarm(self):
        global NewSetting,dbpath,AlarmCfg,trivitem,FileCount
        global Config4alarm,Config4head,Config4durat#,Config4duratinit
        global demo,threadLock,thread4GetColumn,stopFlag,chx_sel,GroupSet
        global gainDict,Opt2ActFrm,StatusBar
        StatusBar = GetGlobals('StatusBar')
        #'Save4Alarm_til = MFOGJHKGLDOEDGOGNHCGAFLHGGDG'
        #'Save4Alarm_txt = MFOGJHKGLDOEDGOGNHCGAFLHHHLH'
        til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MFOGJHKGLDOEDGOGNHCGAFLHGGDG'),
                    Config4Lan.get(AlarmCfg['lang'], 'MFOGJHKGLDOEDGOGNHCGAFLHHHLH'))
        '''
        til, txt = (
            {
                'zh-TW' : lambda : ("修改確認", "確定儲存設定"),
                'en-US' : lambda : ("Confirm", "OK to save the settings"),
                }.get(AlarmCfg['lang'], lambda : ("修改確認", "確定儲存設定"))())
        '''
        args = [root, til, txt]
        VisualNumPad = CreateVisualKeyboard('askyesno', 'VisualNumPad', args)
        VisualNumPad.focus_set()
        self.wait_window(VisualNumPad)
        _check = bool(VisualNumPad.btn_var.get())
        #if tkmsgbox.askyesno(til, txt, parent = self):

        if _check :
            #Opt2ActFrm["00001"][2].resetData()
            #resetData()
            #resetData([x for x in GroupSet])
            
            for _ii in GroupSet:
                GroupSet[_ii]['autotrig'] = [None, None, None]
            resetData([_grp for _grp in list(StatusBar.showgrouplnk.keys())])

            db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
            db.execute("PRAGMA journal_mode=WAL")
            cursor  = db.cursor()
            
            _ret = []
            #NewSetting['reffreq'] = self.Reffreq_variable.get()
            #arString = "%1d" %self.Alarm_light_var.get() + "%1d" %self.Alarm_bee_var.get() + "%1d" %self.Alarm_mail_var.get()
            #NewSetting['alarm_type'] = int(arString,2)
            NewSetting['maxpoint'] = self.PDTimes_variable.get()
            NewSetting['maxdurat'] = self.PDDurat_variable.get()
            #NewSetting['isfilter'] = self.isfilter_var.get()
            #_ret = [NewSetting['reffreq'], NewSetting['alarm_type'], NewSetting['maxpoint'], NewSetting['maxdurat']]
            #cmd_line = 'update alarmcfg set reffreq = ?, alarm_type = ?, maxpoint = ?, maxdurat = ? '
            _ret = [NewSetting['maxpoint'], NewSetting['maxdurat']]#, NewSetting['isfilter']]
            cmd_line = 'update alarmcfg set maxpoint = ?, maxdurat = ?'#, isfilter = ? '

            cmd_line = cmd_line + "where sn = '00001'"
            cursor.execute(cmd_line, _ret)

            for j in GroupSet:
                _ret = []
                _trigChx = vars(self)[('Gr%s_Conf' %j)].Grx_trigChx.get()
                _trigLv = trivitem[vars(self)[('Gr%s_Conf' %j)].Grx_trigLv.get()]
                _v = _s = _g = ''
                _i = 0
                for i in GroupSet[j]['ch']:
                    _g = _g +('%s' %(gainDict[vars(self)[('Ch%s_gain_variable' %i)].get()][_i]))
                    _v = _v +('%s' %vars(self)[('Ch%s_var' %i)].get())
                    _s = _s +('%s' %sensors[vars(self)[('Ch%s_sensor_variable' %i)].get()][0])
                    _i = _i +1
                    
                _ret = [_trigChx, _trigLv, int(_g, 2), int(_v, 2), int(_s, 16), j]
                #print(_ret) #[16, 600.0, 126, 3, 36, 0] [16, 200.0, 126, 3, 36, 1] [16, 200.0, 126, 3, 36, 2]

                GroupSet[j]['trig_ch'] =  _trigChx
                GroupSet[j]['trig_lv'] = _trigLv
                GroupSet[j]['gain'] = int(_g, 2)
                #print(GroupSet[j]['gain'])
                GroupSet[j]['view'] = int(_v, 2)
                GroupSet[j]['sensor'] = int(_s, 16)
                GroupSet[j]['cmdline'] = bytearray([
                    GroupSet[j]['trig_ch'],
                    #int((GroupSet[j]['trig_lv']*0.1) +129.04),
                    int((GroupSet[j]['trig_lv'] +741.7) /7.6),
                    GroupSet[j]['wave_out'],
                    GroupSet[j]['fft_out'],
                    GroupSet[j]['prpd_out'],
                    GroupSet[j]['twmap_out'],
                    GroupSet[j]['sync_opt'],
                    GroupSet[j]['list_choose'],
                    GroupSet[j]['gain']
                    ])
                '''
                print([
                    GroupSet[j]['trig_ch'],
                    #int((GroupSet[j]['trig_lv']*0.1) +129.04),
                    int((GroupSet[j]['trig_lv'] +741.7) /7.6),
                    GroupSet[j]['wave_out'],
                    GroupSet[j]['fft_out'],
                    GroupSet[j]['prpd_out'],
                    GroupSet[j]['twmap_out'],
                    GroupSet[j]['sync_opt'],
                    GroupSet[j]['list_choose'],
                    GroupSet[j]['gain']
                    ])
                '''
                cursor.execute('update adc_setting set trig_ch = ?, trig_lv = ?, gain = ?, view = ?, sensor = ? where sn = ?', _ret)
                ##with open ((curPath +('//cmdline_g%s.~' %j)), 'wb+') as f:
                    ##f.write(GroupSet[j]['cmdline'])
                ##f.close()
                GroupSet[j]['cmdfp'].seek(0)
                GroupSet[j]['cmdfp'].write(GroupSet[j]['cmdline'])
                #print("GroupSet[j]['cmdfp'] : ", bytearray(GroupSet[j]['cmdfp'][:]))
                #GroupSet[j]['cmdfp'] :  bytearray(b'\x10\xb0\x01\x01\x01\x01\x02\x00~')
                #GroupSet[j]['cmdfp'] :  bytearray(b'\x10{\x01\x01\x01\x01\x02\x00~')
                #GroupSet[j]['cmdfp'] :  bytearray(b'\x10{\x01\x01\x01\x01\x02\x00~')

            #db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
            #db.execute("PRAGMA journal_mode=WAL")
            #cursor  = db.cursor()
            #cursor.execute(cmd_line, _ret)

            db.commit()
            cursor.execute("select * from alarmcfg")
            #fnames = list(map(lambda x: x[0], cursor.description))
            alarm_res = cursor.fetchone()
            adc_res = cursor.fetchall()
            cursor.close()
            db.close()
            ##del Config4alarm,Config4durat#,Config4duratinit
            ##Config4alarm = ConfigLib.ConfigParser()
            ##Config4durat = ConfigLib.ConfigParser()
            #Config4duratinit = ConfigLib.ConfigParser()
            ##{ x: GroupSet[x]['ln'].clear() for x in GroupSet}   #清空GroupSet[x]['ln']
            global loadconfig
            loadconfig.getAlarmcfg(alarm_res)  #輸出參數

    def actNumPad(self, para):
        global subClass,subform
        obj = para[0]
        text = para[1]

        args = [self, obj, text,]
        VisualNumPad = CreateVisualKeyboard('VisualNumKeyboard', 'VisualNumPad', args)
        VisualNumPad.focus_set()
        #VisualNumPad.bind('<FocusOut>', lambda widget: self.closetoplevel(VisualNumPad))

    '''
    def actFltPad(self, para):
        global VisualNumPad,subClass,subform
        obj = para[0]
        text = para[1]

        globals().update(refreshGlobals())
        try:
            VisualNumPad.destroy()
        except:
            pass
        
        #VisualNumPad = VisualFltKeyboard(self, obj, text)
        VisualNumPad = subClass.VisualFltKeyboard(self, obj, text)
        VisualNumPad.focus_set()
        VisualNumPad.bind('<FocusOut>', lambda widget: self.closetoplevel(VisualNumPad))
    '''
    def closetoplevel(self, widget):
        widget.destroy()

#=================================================================
#========================= Advanced Frame ==========================
class AdvancedFrm(tk.Frame):
    def __init__(self, parent, controller, law):
        global root,AlarmCfg#,bee_pin,gr_pin,yl_pin,Ch1_LPIN,Ch1_HPIN,Ch2_LPIN,Ch2_HPIN,Ch3_LPIN,Ch4_LPIN
        #global demo,sync,chk_0_Img,chk_1_Img,chx_sel,Opt2ActFrm,thisOS,comportlist
        
        tk.Frame.__init__(self,parent)
        self.parent = parent
        h = self.parent['height'] -tilBar['height'] -StatusBar['height']
        self.config(relief = tk.GROOVE, bg = '#ffffff', width = self.parent['width'] -40, height = h)
        self.place(x = 0, y = tilBar['height'])
        self.law = law
        #self.pi = self.place_info()

        '''
        if thisOS == 'Windows' :
            btnW = 8
        elif thisOS == 'Linux' :
            btnW = 7
        '''
        btnW = 7

        self.gpio = {}
        self.setgpio4bee = tk.Button(self, text='bee_pin', font = ('IPAGothic', 13, 'bold'),
                                     image = '', compound="center", width = btnW)
        self.setgpio4bee.config(command = lambda obj = self.setgpio4bee: self.getGPIO(obj))
        self.setgpio4bee.config(relief = tk.RAISED, bd = 2)
        self.gpio['bee_pin'] = tk.IntVar()
        self.gpio['bee_pin'].set(AlarmCfg['bee_pin'])
        self.gpio4bee = tk.Entry(self, bd = 2, textvariable = self.gpio['bee_pin'],
                                 font = ('IPAGothic', 18, 'bold'),width = 3, state = tk.DISABLED,
                                 disabledbackground = '#ffffff', disabledforeground = '#000000')
        
        self.setgpio4yl = tk.Button(self, text='yl_pin', font = ('IPAGothic', 13, 'bold'),
                                    image = '', compound="center", width = btnW)
        self.setgpio4yl.config(command = lambda obj = self.setgpio4yl: self.getGPIO(obj))
        self.setgpio4yl.config(relief = tk.RAISED, bd = 2)
        self.gpio['yl_pin'] = tk.IntVar()
        self.gpio['yl_pin'].set(AlarmCfg['yl_pin'])
        self.gpio4yl = tk.Entry(self, bd = 2, textvariable = self.gpio['yl_pin'],
                                font = ('IPAGothic', 18, 'bold'),width = 3, state = tk.DISABLED,
                                disabledbackground = '#ffffff', disabledforeground = '#000000')

        '''
        self.setgpio4Ch1_H = tk.Button(self, text='sync_PIN', font = ('IPAGothic', 13, 'bold'),
                                       image = '', compound="center", width = btnW)
        self.setgpio4Ch1_H.config(command = lambda obj = self.setgpio4Ch1_H: self.getGPIO(obj))
        self.setgpio4Ch1_H.config(relief = tk.RAISED, bd = 2)
        self.gpio['Ch1_HPIN'] = tk.IntVar()
        self.gpio['Ch1_HPIN'].set(AlarmCfg['Ch1_HPIN'])
        self.gpio4Ch1_H = tk.Entry(self, bd = 2, textvariable = self.gpio['Ch1_HPIN'],
                                   font = ('IPAGothic', 18, 'bold'),width = 3, state = tk.DISABLED,
                                   disabledbackground = '#ffffff', disabledforeground = '#000000')

        self.setgpio4Ch1_L = tk.Button(self, text='Ch1_LPIN', font = ('IPAGothic', 13, 'bold'),
                                       image = '', width = btnW)
        self.setgpio4Ch1_L.config(command = lambda obj = self.setgpio4Ch1_L: self.getGPIO(obj))
        self.setgpio4Ch1_L.config(relief = tk.RAISED, bd = 2)
        self.gpio['Ch1_LPIN'] = tk.IntVar()
        self.gpio['Ch1_LPIN'].set(AlarmCfg['Ch1_LPIN'])
        self.gpio4Ch1_L = tk.Entry(self, bd = 2, textvariable = self.gpio['Ch1_LPIN'],
                                   font = ('IPAGothic', 18, 'bold'),width = 3, state = tk.DISABLED,
                                   disabledbackground = '#ffffff', disabledforeground = '#000000')

        self.setgpio4Ch2_L = tk.Button(self, text='Ch2_LPIN', font = ('IPAGothic', 13, 'bold'),
                                       image = '', compound="center", width = btnW)
        self.setgpio4Ch2_L.config(command = lambda obj = self.setgpio4Ch2_L: self.getGPIO(obj))
        self.setgpio4Ch2_L.config(relief = tk.RAISED, bd = 2)
        self.gpio['Ch2_LPIN'] = tk.IntVar()
        self.gpio['Ch2_LPIN'].set(AlarmCfg['Ch2_LPIN'])
        self.gpio4Ch2_L = tk.Entry(self, bd = 2, textvariable = self.gpio['Ch2_LPIN'],
                                   font = ('IPAGothic', 18, 'bold'),width = 3, state = tk.DISABLED,
                                   disabledbackground = '#ffffff', disabledforeground = '#000000')

        self.setgpio4Ch3_L = tk.Button(self, text='Ch3_LPIN', font = ('IPAGothic', 13, 'bold'),
                                       image = '', compound="center", width = btnW)
        self.setgpio4Ch3_L.config(command = lambda obj = self.setgpio4Ch3_L: self.getGPIO(obj))
        self.setgpio4Ch3_L.config(relief = tk.RAISED, bd = 2)
        self.gpio['Ch3_LPIN'] = tk.IntVar()
        self.gpio['Ch3_LPIN'].set(AlarmCfg['Ch3_LPIN'])
        self.gpio4Ch3_L = tk.Entry(self, bd = 2, textvariable = self.gpio['Ch3_LPIN'],
                                   font = ('IPAGothic', 18, 'bold'),width = 3, state = tk.DISABLED,
                                   disabledbackground = '#ffffff', disabledforeground = '#000000')

        self.setgpio4Ch4_L = tk.Button(self, text='Ch4_LPIN', font = ('IPAGothic', 13, 'bold'),
                                       image = '', compound="center", width = btnW)
        self.setgpio4Ch4_L.config(command = lambda obj = self.setgpio4Ch4_L: self.getGPIO(obj))
        self.setgpio4Ch4_L.config(relief = tk.RAISED, bd = 2)
        self.gpio['Ch4_LPIN'] = tk.IntVar()
        self.gpio['Ch4_LPIN'].set(AlarmCfg['Ch4_LPIN'])
        self.gpio4Ch4_L = tk.Entry(self, bd = 2, textvariable = self.gpio['Ch4_LPIN'],
                                   font = ('IPAGothic', 18, 'bold'),width = 3, state = tk.DISABLED,
                                   disabledbackground = '#ffffff', disabledforeground = '#000000')
        '''
        
        #self.demolist = [0, 1, 2, 3, 4, 5, 6, 7, 90, 91, 92, 93, 94, 95, 96, 97]
        self.demolist = [0, 2, 95, 98, 99]
        self.demovar = tk.IntVar()
        self.demovar.set(AlarmCfg['demo'])
        self.demolbl = tk.Label(self, text = 'demo', font = ('IPAGothic', 13, 'bold'),
                                bg = '#ffffff')
        self.demo = tk.OptionMenu(self, self.demovar, *self.demolist)
        self.demo.config(font = ('IPAGothic', 15, 'bold'))
        self.demo['menu'].config(font = ('IPAGothic', 13, 'bold'))

        self.beetypelist = [3, 0]
        self.beetypevar = tk.IntVar()
        self.beetypevar.set(AlarmCfg['Ch1_LPIN'])
        self.beetypelbl = tk.Label(self, text = 'b-type', font = ('IPAGothic', 13, 'bold'),
                                bg = '#ffffff')
        self.beetype = tk.OptionMenu(self, self.beetypevar, *self.beetypelist)
        self.beetype.config(font = ('IPAGothic', 15, 'bold'))
        self.beetype['menu'].config(font = ('IPAGothic', 13, 'bold'))
        
        '''
        self.syncvar = tk.IntVar()
        self.syncvar.set(AlarmCfg['sync'])
        self.sync = tk.Checkbutton(self, variable = self.syncvar,
                                   bd = 0, relief = tk.FLAT, image = chk_0_Img,
                                   selectimage = chk_1_Img, onvalue = 1,
                                   offvalue = 0)
        self.sync.config(activebackground = "#ffffff",bg = "#ffffff", indicatoron  = 0)
        self.sync.config(compound = tk.LEFT, state = tk.NORMAL)

        self.sync.config(text = 'sync', font = ('IPAGothic', 13, 'bold'))
        '''

        self.chx_selvar = tk.IntVar()
        self.chx_selvar.set(AlarmCfg['chx_sel'])
        self.chx_sel = tk.Checkbutton(self, variable = self.chx_selvar,
                                      bd = 0, relief = tk.FLAT, image = chk_0_Img,
                                      selectimage = chk_1_Img, onvalue = 1,
                                      offvalue = 0)
        self.chx_sel.config(activebackground = "#ffffff",bg = "#ffffff", indicatoron  = 0)
        self.chx_sel.config(compound = tk.LEFT, state = tk.NORMAL)
        self.chx_sel.config(text = 'Single Alarm', font = ('IPAGothic', 13, 'bold'))

        self.verlist = [0, 1, 2, 3]
        self.verselvar = tk.IntVar()
        self.verselvar.set(AlarmCfg['ver_sel'])
        '''
        self.versellbl = tk.Label(self, text = 'ver.', font = ('IPAGothic', 13, 'bold'),
                                  bg = '#ffffff')
        self.versel = tk.OptionMenu(self, self.verselvar, *self.verlist, command = self.ui_ver_sel)
        self.versel.config(font = ('IPAGothic', 15, 'bold'))
        self.versel['menu'].config(font = ('IPAGothic', 13, 'bold'))
        '''
        self.loginlawlist = [0, 1, 2]
        self.loginlawvar = tk.IntVar()
        self.loginlawvar.set(AlarmCfg['loginlaw'])
        self.loginlawlbl = tk.Label(self, text = 'loginlaw', font = ('IPAGothic', 13, 'bold'),
                                    bg = '#ffffff')
        self.loginlawsel = tk.OptionMenu(self, self.loginlawvar, *self.loginlawlist, command = self.chg_init_law)
        self.loginlawsel.config(font = ('IPAGothic', 15, 'bold'))
        self.loginlawsel['menu'].config(font = ('IPAGothic', 13, 'bold'))

        #'cleanhistory = MGDGKGOGBGHGGGMHLHAGNHGH'
        self.cleanhistory = tk.Button(self, text= Config4Lan.get(AlarmCfg['lang'], 'MGDGKGOGBGHGGGMHLHAGNHGH'))
        '''
        self.cleanhistory = tk.Button(self, text=
                                      {
                                          'zh-TW' : lambda : "清除資料",
                                          'en-US' : lambda : "Clean Data",
                                          }.get(AlarmCfg['lang'], lambda : "清除資料")())
        '''
        self.cleanhistory.config(font = ('IPAGothic', 13, 'bold'), compound="center",
                                 command = self.cleanhist, width = 11)
        self.cleanhistory.config(relief = tk.RAISED, bd = 2)

        #'reset4adv = NHKGMHKGLHLDOGLGJH'
        self.reset = tk.Button(self, text = Config4Lan.get(AlarmCfg['lang'], 'NHKGMHKGLHLDOGLGJH'))
        '''
        self.reset = tk.Button(self, text=
                               {
                                   'zh-TW' : lambda : "載初始值",
                                   'en-US' : lambda : "Load Default",
                                   }.get(AlarmCfg['lang'], lambda : "載初始值")())
        '''
        self.reset.config(font = ('IPAGothic', 13, 'bold'), compound="center",
                                 command = self.loaddefault, width = 11)
        self.reset.config(relief = tk.RAISED, bd = 2)

        #'PINTest = PFGEBELFKGMHLH'
        '''
        self.PINTest = tk.Button(self, text = Config4Lan.get(AlarmCfg['lang'], 'PFGEBELFKGMHLH'))
        self.PINTest = tk.Button(self, text=
                                 {
                                     'zh-TW' : lambda : "腳位測試",
                                     'en-US' : lambda : "PIN Check",
                                     }.get(AlarmCfg['lang'], lambda : "腳位測試")())
        '''
        '''
        self.PINTest.config(font = ('IPAGothic', 13, 'bold'), compound="center",
                                 command = self.PWMTest, width = 11)
        self.PINTest.config(relief = tk.RAISED, bd = 2)
        '''
        '''
        self.syncTestBtn = tk.Button(self, text=
                                     {
                                         'zh-TW' : lambda : "工頻測試",
                                         'en-US' : lambda : "Sync Test",
                                         }.get(AlarmCfg['lang'], lambda : "工頻測試")())
        self.syncTestBtn.config(font = ('IPAGothic', 13, 'bold'), compound="center",
                                command = self.syncTest, width = 11)
        self.syncTestBtn.config(relief = tk.RAISED, bd = 2)
        '''
        self.showlogBtn = tk.Button(self, text=
                                    {
                                        'zh-TW' : lambda : "err log.",
                                        'en-US' : lambda : "err log.",
                                        }.get(AlarmCfg['lang'], lambda : "err log.")())
        self.showlogBtn.config(font = ('IPAGothic', 13, 'bold'), compound="center",
                               command = self.showlog, width = 11)
        self.showlogBtn.config(relief = tk.RAISED, bd = 2)

        self.isIdlesupportvar = tk.IntVar()
        self.isIdlesupportvar.set(AlarmCfg['isIdlesupport'])
        self.isIdlesupport = tk.Checkbutton(self, variable = self.isIdlesupportvar,
                                            bd = 0, relief = tk.FLAT, image = chk_0_Img,
                                            selectimage = chk_1_Img, onvalue = 1,
                                            offvalue = 0)
        self.isIdlesupport.config(activebackground = "#ffffff",bg = "#ffffff", indicatoron  = 0)
        self.isIdlesupport.config(compound = tk.LEFT, state = tk.NORMAL)
        self.isIdlesupport.config(text = 'Support Idle Limit', font = ('IPAGothic', 13, 'bold'))

        self.ADportFrm = tk.LabelFrame(self, relief = tk.GROOVE, bg = self['bg'],
                                       text = 'Group and Serial Port setting',
                                       font = ('IPAGothic', 13, 'bold'),
                                       bd = 2,
                                       height = 100, width = 440)
        
        Save4AdvancedBtn = tk.Button(self, text='', font = ('IPAGothic', 13, 'bold'), image = icon4Save,
                                  compound="center", command = self.Save4Advanced)
        Save4AdvancedBtn.config(activebackground = "#ffffff", bg = '#ffffff', relief = tk.FLAT, bd = 0)
        
        self.setgpio4bee.place(x = 5, y = 5)
        self.gpio4bee.place(x = 110, y = 5)
        self.setgpio4yl.place(x = 5, y = 45)
        self.gpio4yl.place(x = 110, y = 45)
        '''
        self.setgpio4Ch1_H.place(x = 5, y = 85)
        self.gpio4Ch1_H.place(x = 110, y = 85)
        self.setgpio4Ch1_L.place(x = 170, y = 5)
        self.gpio4Ch1_L.place(x = 275, y = 5)
        self.setgpio4Ch2_L.place(x = 170, y = 45)
        self.gpio4Ch2_L.place(x = 275, y = 45)
        self.setgpio4Ch3_L.place(x = 170, y = 85)
        self.gpio4Ch3_L.place(x = 275, y = 85)
        self.setgpio4Ch4_L.place(x = 170, y = 125)
        self.gpio4Ch4_L.place(x = 275, y = 125)
        self.demolbl.place(x = 335, y = 10)
        self.demo.place(x = 385, y = 5)
        self.sync.place(x = 335, y = 45)
        self.chx_sel.place(x = 335, y = 85)
        self.versellbl.place(x = 335, y = 135)
        self.versel.place(x = 385, y = 125)
        self.cleanhistory.place(x = 460, y= 5)
        self.reset.place(x = 460, y= 45)
        self.PINTest.place(x = 460, y = 85)
        self.syncTestBtn.place(x = 460, y = 125)
        self.showlogBtn.place(x = 460, y = 165)
        '''
        self.demolbl.place(x = 5, y = 90)
        self.demo.place(x = 100, y = 85)
        self.beetypelbl.place(x = 5, y = 130)
        self.beetype.place(x = 70, y = 125)
        self.chx_sel.place(x = 5, y = 165)
        #self.versellbl.place(x = 5, y = 130)
        #self.versel.place(x = 100, y = 125)
        self.loginlawlbl.place(x = 5, y = 210)
        self.loginlawsel.place(x = 100, y = 205)
        self.cleanhistory.place(x = 170, y= 5)
        self.reset.place(x = 170, y= 45)
        #self.PINTest.place(x = 170, y = 85)
        self.showlogBtn.place(x = 170, y = 125)
        self.isIdlesupport.place(x = 170, y = 165)
        self.ADportFrm.place(x = 335, y =5)
        Save4AdvancedBtn.place(x = self['width'] -125, y = self['height'] -Save4AdvancedBtn.winfo_reqheight())

        self.editdevice()

        if self.law >0:
            loginlaw = GetGlobals('loginlaw')
            UpdateOptStates(self, int(self.law <= loginlaw))

    def editdevice(self):
        global curPath,dbpath,AlarmCfg
        self.title = {
            0:['sn', 'sn', 1],
            1:['port', 'port', 1],
            2:['baudrate', 'baudrate',1],
            #3:['bytesize', 'bytesize',1],
            #4:['parity', 'parity',1],
            #5:['stopbits', 'stopbits', 1],
            #6:['timeout', 'timeout', 1]
            }
        
        db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
        db.execute("PRAGMA journal_mode=WAL")
        cursor  = db.cursor()
        cursor.execute("select * from adc_setting")
        fnames = list(map(lambda x: x[0], cursor.description))
        res = cursor.fetchall() #取得記錄數
        cursor.close()
        db.close()

        i = 0
        j = 0
        Headbtns = []
        GridCol = []
        ColW = []
        RowH = 0
        oLf = 0

        para = []
        [para.append([idx for idx in range(len(fnames)) if fnames[idx] == self.title[x][0]][0]) for x in self.title]
        self.counter = []

        for j in range(len(res) +1):
            if j >0:
                GridCol.append([])
                rec = [[self.title[ti][0] , res[(j -1)][(para[ti])]] for ti in range(len(self.title))]
                _sn = [item[1] for item in rec if item[0] == 'sn'][0]

            for i in self.title:
                idx = fnames.index(self.title[i][0])

                if j == 0:
                    fn = fnames[idx]
                    
                    if self.title[i][2] >0:
                        Headbtns.append(tk.Button(self.ADportFrm, text = self.title[i][1], font = ('IPAGothic', 10, 'bold'),
                                                  fg = "#0000ff", anchor = tk.W))

                        ColW.append(Headbtns[-1].winfo_reqwidth())
                        #Headbtns[-1].place(x = sum(ColW[:-1]), y = 0)
                        if i == 0:
                            RowH = RowH +Headbtns[-1].winfo_reqheight()
                    else:
                        Headbtns.append(None)
                        ColW.append(0)

                else:
                    t = res[(j-1)][idx]
                    if type(t) == float:
                        t = '%.2f' %t

                    if self.title[i][2] >0:
                        GridCol[-1].append(tk.Button(self.ADportFrm, text = t, font = ('IPAGothic', 10, 'bold'),
                                                     fg = "#000000", anchor = tk.W,
                                                     command = lambda sn = _sn : self.adc_set(sn)))
                        GridCol[-1][-1].grid(column =i, row =(j +1), sticky =tk.N +tk.E +tk.W +tk.S)

                        if GridCol[-1][-1].winfo_reqwidth() > ColW[i]:
                            ColW[i] = GridCol[-1][-1].winfo_reqwidth()

                            for jj in range(j):
                                #GridCol[jj][i].place(x = sum(ColW[:i]), y = (jj +1) *25, width = ColW[i])
                                pass
                        else:
                            #GridCol[-1][-1].place(x = sum(ColW[:i]), y = (j) *25, width = ColW[i])
                            pass
                        #Headbtns[i].place(x = sum(ColW[:i]), y = 0, width = ColW[i])
                        Headbtns[i].grid(column =i, row =0, sticky =tk.N +tk.E +tk.W +tk.S)
                        if i == 0:
                            RowH = RowH +GridCol[-1][-1].winfo_reqheight()

                    else:
                        GridCol[-1].append(None)

        self.ADportFrm.config(width = sum(ColW) +5)
        self.ADportFrm.config(height= RowH +15)

    def adc_set(self, sn):
        #args = [self.parent, sn,]
        #VisualNumPad = CreateVisualKeyboard('ADCSetting', 'VisualNumPad', args)
        self.adcfrm = ADCSetting(self.parent, sn)
        pass

    def setcolor(self):
        #print(colorchooser.askcolor())
        pass

    def ui_ver_sel(self, value):
        #print(value)
        pass

    def chg_init_law(self, value):
        pass

    def showlog(self):
        global status,lang,StatusBar,tilBar#,VisualNumPad
        global Opt2ActFrm,GPIO

        if status == 0:
            UpdateOptStates(tilBar, 0)
            UpdateOptStates(StatusBar, 0)
            UpdateOptStates(self, 0)
            thisFrm = tilBar.control_variable.get()
            lKey = [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if thisFrm in x][0])][0]
            UpdateOptStates(Opt2ActFrm[lKey][2], 0)
            
            args = [self,]
            VisualNumPad = CreateVisualKeyboard('ErrlogForm', 'VisualNumPad', args)
            VisualNumPad.focus_set()
        else:
            #'Stop_til : MFLHAGPHAFLHGGDG'
            #'Stop_txt : MFLHAGPHAFLHHHLH'
            til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MFLHAGPHAFLHGGDG'),
                        Config4Lan.get(AlarmCfg['lang'], 'MFLHAGPHAFLHHHLH'))
            '''
            til, txt = (
                {
                    'zh-TW' : lambda : ("訊息", "請先暫停測試"),
                    'en-US' : lambda : ("Information", "Please Stop First."),
                    }.get(AlarmCfg['lang'], lambda : ("訊息", "請先暫停測試"))())
            '''
        pass

    '''
    def syncTest(self):
        global status,lang,StatusBar,tilBar
        global Opt2ActFrm,GPIO

        if status == 0:
            UpdateOptStates(tilBar, 0)
            UpdateOptStates(StatusBar, 0)
            UpdateOptStates(self, 0)
            thisFrm = tilBar.control_variable.get()
            lKey = [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if thisFrm in x][0])][0]
            UpdateOptStates(Opt2ActFrm[lKey][2], 0)

            args = [self,]
            VisualNumPad = CreateVisualKeyboard('SyncTestForm', 'VisualNumPad', args)
            VisualNumPad.focus_set()
        else:
            til, txt = (
                {
                    'zh-TW' : lambda : ("訊息", "請先暫停測試"),
                    'en-US' : lambda : ("Information", "Please Stop First."),
                    }.get(AlarmCfg['lang'], lambda : ("訊息", "請先暫停測試"))())
    '''
    
    def cleanhist(self):
        global lang,curPath,linkfile,dbpath,thisOS,showerrorFrm,showerrorFrm
        global History,GroupSet
        #'cleanhistChk_til = MGDGKGOGBGHGGGMHLHMEHGEGAFLHGGDG'
        #'cleanhistChk_txt = MGDGKGOGBGHGGGMHLHMEHGEGAFLHHHLH'
        til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MGDGKGOGBGHGGGMHLHMEHGEGAFLHGGDG'),
                        Config4Lan.get(AlarmCfg['lang'], 'MGDGKGOGBGHGGGMHLHMEHGEGAFLHHHLH'))
        '''
        til, txt = (
            {
                'zh-TW' : lambda : ("警告", "將會清除所有測試資料\n"+ "請確認？"),
                'en-US' : lambda : ("Warning", "Will Clean all Records.\n"+ "Check again Please."),
                }.get(AlarmCfg['lang'], lambda : ("警告", "將會清除所有測試資料\n"+ "請確認？"))())
        '''

        args = [root, til, txt]
        VisualNumPad = CreateVisualKeyboard('askyesno', 'VisualNumPad', args)
        VisualNumPad.focus_set()
        self.wait_window(VisualNumPad)
        _check = bool(VisualNumPad.btn_var.get())
        if _check :
        #if tkmsgbox.askyesno(til, txt, parent = self, icon = tkmsgbox.WARNING):
            '''
            delfilelist = ['*.pdd', '*.cfg', '*.col', '*.spl', '*.bak', '*.tmp']
            for l in delfilelist:
                fl = curPath + '//'+ l
                for f in glob.glob(fl):
                    if ((os.path.splitext(os.path.basename(f))[0]) !=
                        (os.path.splitext(os.path.basename((curPath + '//' + linkfile)))[0])):
                        os.remove(f)
            db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
            db.execute("PRAGMA journal_mode=WAL")
            cursor = db.cursor()
            cursor.execute("delete from bootlog")
            cursor.execute("delete from history")
            db.commit()
            cursor.close()
            db.close()
            '''
            History = GetGlobals('History')
            GroupSet = GetGlobals('GroupSet')
            for key in list(History.keys()):
                History[key].close()
            for i in GroupSet:
                if type(GroupSet[i]['trend']['mv']['fd']) == mmap.mmap:
                    GroupSet[i]['trend']['mv']['fd'].close()
                if type(GroupSet[i]['trend']['counters']['fd']) == mmap.mmap:
                    GroupSet[i]['trend']['counters']['fd'].close()
                mmap_k = list(GroupSet[i]['mmap'].keys())
                for _mi in range(0, len(mmap_k)):
                    GroupSet[i]['mmap'][mmap_k[_mi]].close()

            if thisOS == 'Windows' :
                commLine = 'python ' + curPath + '//cleanhist.py'
            elif thisOS == 'Linux' :
                commLine = ('sudo python3 ' + curPath + '//cleanhist.py%s') %('c' *int(os.path.isfile(curPath + '//cleanhist.pyc')))
                #commLine = 'sudo python3 ' + curPath + '//cleanhist.py'
            p = subprocess.Popen(commLine, stdout = subprocess.PIPE, shell = True)
            out = p.communicate()[0]
            out = int(out.decode('ascii'))
            if out == 1:
                #'cleanhistSus_til = MGDGKGOGBGHGGGMHLHMFKHMHAFLHGGDG'
                #'cleanhistSus_txt = MGDGKGOGBGHGGGMHLHMFKHMHAFLHHHLH'
                til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MGDGKGOGBGHGGGMHLHMFKHMHAFLHGGDG', vars={'para1':  str(out)}),
                                Config4Lan.get(AlarmCfg['lang'], 'MGDGKGOGBGHGGGMHLHMFKHMHAFLHHHLH'))
                '''
                til, txt = (
                    {
                        'zh-TW' : lambda : ("訊息["+ str(out)+ "]", "已清除所有資料\n" + "請重新啟動"),
                        'en-US' : lambda : ("Information["+ str(out)+ "]", "All records has been deleted.\n" + "Please Restart."),
                        }.get(AlarmCfg['lang'], lambda : ("訊息["+ str(out)+ "]", "已清除所有資料\n" + "請重新啟動"))())
                '''
                #tkmsgbox.showinfo(til, txt, parent = self)
                '''
                args = [root, til, txt]
                VisualNumPad = CreateVisualKeyboard('showinfo', 'VisualNumPad', args)
                VisualNumPad.focus_set()
                self.wait_window(VisualNumPad)
                '''
                showerrorFrm = GetGlobals('showerrorFrm')
                showerrorFrm.msg_var.set(txt)
                showerrorFrm.updatepos('info')
                showerrorFrm.tkraise()
            else:
                #'cleanhistErr_til = MGDGKGOGBGHGGGMHLHKENHNHAFLHGGDG'
                #'cleanhistErr_txt = MGDGKGOGBGHGGGMHLHKENHNHAFLHHHLH'
                til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MGDGKGOGBGHGGGMHLHKENHNHAFLHGGDG', vars={'para1':  str(out)}),
                                Config4Lan.get(AlarmCfg['lang'], 'MGDGKGOGBGHGGGMHLHKENHNHAFLHHHLH'))
                '''
                til, txt = (
                    {
                        'zh-TW' : lambda : ("錯誤["+ str(out)+ "]", "錯誤\n"),
                        'en-US' : lambda : ("Error["+ str(out)+ "]", "Error\n"),
                        }.get(AlarmCfg['lang'], lambda : ("錯誤["+ str(out)+ "]", "錯誤\n"))())
                '''
                #tkmsgbox.showerror(til, txt, parent = self)
                '''
                args = [root, til, txt]
                VisualNumPad = CreateVisualKeyboard('showerror', 'VisualNumPad', args)
                VisualNumPad.focus_set()
                self.wait_window(VisualNumPad)
                '''
                showerrorFrm = GetGlobals('showerrorFrm')
                showerrorFrm.msg_var.set(txt)
                showerrorFrm.updatepos('err')
                showerrorFrm.tkraise()
        pass

    def loaddefault(self):
        global lang,curPath,linkfile,dbpath,thisOS,tilBar,showerrorFrm,showerrorFrm
        #'loaddefaultChk_til = DGAGOGLGLGKGJGOGKHDGLHMEHGEGAFLHGGDG'
        #'loaddefaultChk_txt = DGAGOGLGLGKGJGOGKHDGLHMEHGEGAFLHHHLH'
        til, txt = (Config4Lan.get(AlarmCfg['lang'], 'DGAGOGLGLGKGJGOGKHDGLHMEHGEGAFLHGGDG'),
                        Config4Lan.get(AlarmCfg['lang'], 'DGAGOGLGLGKGJGOGKHDGLHMEHGEGAFLHHHLH'))
        '''
        til, txt = (
            {
                'zh-TW' : lambda : ("警告", "將會回復預設值\n"+ "請確認？"),
                'en-US' : lambda : ("Warning", "Will be Reseted to Default.\n"+ "Check again Please."),
                }.get(AlarmCfg['lang'], lambda : ("警告", "將會回復預設值\n"+ "請確認？"))())
        '''
        args = [root, til, txt]
        VisualNumPad = CreateVisualKeyboard('askyesno', 'VisualNumPad', args)
        VisualNumPad.focus_set()
        self.wait_window(VisualNumPad)
        _check = bool(VisualNumPad.btn_var.get())
        if _check :
        #if tkmsgbox.askyesno(til, txt, parent = self, icon = tkmsgbox.WARNING):
            if thisOS == 'Windows' :
                commLine = 'python ' + curPath + '//loaddefault.py'
            elif thisOS == 'Linux' :
                commLine = ('sudo python3 ' + curPath + '//loaddefault.py%s') %('c' *int(os.path.isfile(curPath + '//loaddefault.pyc')))
                #commLine = 'sudo python3 ' + curPath + '//loaddefault.py'
            p = subprocess.Popen(commLine, stdout = subprocess.PIPE, shell = True)
            out = p.communicate()[0]
            out = int(out.decode('ascii'))
            if out == 1:
                ActivePage(tilBar.control_variable.get())
                #'loaddefaultSus_til = DGAGOGLGLGKGJGOGKHDGLHMFKHMHAFLHGGDG'
                #'loaddefaultSus_txt = DGAGOGLGLGKGJGOGKHDGLHMFKHMHAFLHHHLH'
                til, txt = (Config4Lan.get(AlarmCfg['lang'], 'DGAGOGLGLGKGJGOGKHDGLHMFKHMHAFLHGGDG', vars={'para1':  str(out)}),
                                Config4Lan.get(AlarmCfg['lang'], 'DGAGOGLGLGKGJGOGKHDGLHMFKHMHAFLHHHLH'))
                '''
                til, txt = (
                    {
                        'zh-TW' : lambda : ("訊息["+ str(out)+ "]", "已回復預設值\n" + "請重新啟動"),
                        'en-US' : lambda : ("Information["+ str(out)+ "]", "Reseted to Default.\n" + "Please Restart."),
                        }.get(AlarmCfg['lang'], lambda : ("訊息["+ str(out)+ "]", "已回復預設值\n" + "請重新啟動"))())
                '''
                #tkmsgbox.showinfo(til, txt, parent = self)
                '''
                args = [root, til, txt]
                VisualNumPad = CreateVisualKeyboard('showinfo', 'VisualNumPad', args)
                VisualNumPad.focus_set()
                self.wait_window(VisualNumPad)
                '''
                showerrorFrm = GetGlobals('showerrorFrm')
                showerrorFrm.msg_var.set(txt)
                showerrorFrm.updatepos('info')
                showerrorFrm.tkraise()
            else:
                #'cleanhistErr_til = MGDGKGOGBGHGGGMHLHKENHNHAFLHGGDG'
                #'cleanhistErr_txt = MGDGKGOGBGHGGGMHLHKENHNHAFLHHHLH'
                til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MGDGKGOGBGHGGGMHLHKENHNHAFLHGGDG', vars={'para1':  str(out)}),
                                Config4Lan.get(AlarmCfg['lang'], 'MGDGKGOGBGHGGGMHLHKENHNHAFLHHHLH'))
                '''
                til, txt = (
                    {
                        'zh-TW' : lambda : ("錯誤["+ str(out)+ "]", "錯誤\n"),
                        'en-US' : lambda : ("Error["+ str(out)+ "]", "Error\n"),
                        }.get(AlarmCfg['lang'], lambda : ("錯誤["+ str(out)+ "]", "錯誤\n"))())
                '''
                #tkmsgbox.showerror(til, txt, parent = self)
                '''
                args = [root, til, txt]
                VisualNumPad = CreateVisualKeyboard('showerror', 'VisualNumPad', args)
                VisualNumPad.focus_set()
                self.wait_window(VisualNumPad)
                '''
                showerrorFrm = GetGlobals('showerrorFrm')
                showerrorFrm.msg_var.set(txt)
                showerrorFrm.updatepos('err')
                showerrorFrm.tkraise()
            pass
        pass

    def PWMTest(self):
        global status,lang,StatusBar,tilBar
        global Opt2ActFrm,GPIO,showerrorFrm

        if GetGlobals('PINForm') is not None:
            if status == 0:
                UpdateOptStates(tilBar, 0)
                UpdateOptStates(StatusBar, 0)
                UpdateOptStates(self, 0)
                thisFrm = tilBar.control_variable.get()
                lKey = [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if thisFrm in x][0])][0]
                UpdateOptStates(Opt2ActFrm[lKey][2], 0)

                args = [self,]
                VisualNumPad = CreateVisualKeyboard('PINForm', 'VisualNumPad', args)
                VisualNumPad.focus_set()

            else:
                #'Stop_til : MFLHAGPHAFLHGGDG'
                #'Stop_txt : MFLHAGPHAFLHHHLH'
                til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MFLHAGPHAFLHGGDG'),
                            Config4Lan.get(AlarmCfg['lang'], 'MFLHAGPHAFLHHHLH'))
                '''
                til, txt = (
                    {
                        'zh-TW' : lambda : ("訊息", "請先暫停測試\n"),
                        'en-US' : lambda : ("Information", "Please Stop First.\n"),
                        }.get(AlarmCfg['lang'], lambda : ("訊息", "請先暫停測試\n"))())
                '''
                #tkmsgbox.showerror(til, txt, parent = root)
                '''
                args = [root, til, txt]
                VisualNumPad = CreateVisualKeyboard('showerror', 'VisualNumPad', args)
                VisualNumPad.focus_set()
                self.wait_window(VisualNumPad)
                '''
                showerrorFrm = GetGlobals('showerrorFrm')
                showerrorFrm.msg_var.set(txt)
                showerrorFrm.updatepos('err')
                showerrorFrm.tkraise()
                pass
        else:
            #'PWMTestOsErr_til : PFIFCELFKGMHLHAEMHKENHNHAFLHGGDG'
            #'PWMTestOsErr_txt : PFIFCELFKGMHLHAEMHKENHNHAFLHHHLH'
            til, txt = (Config4Lan.get(AlarmCfg['lang'], 'PFIFCELFKGMHLHAEMHKENHNHAFLHGGDG'),
                        Config4Lan.get(AlarmCfg['lang'], 'PFIFCELFKGMHLHAEMHKENHNHAFLHHHLH'))
            '''
            til, txt = (
                {
                    'zh-TW' : lambda : ("錯誤", "作業系統錯誤\n"),
                    'en-US' : lambda : ("Error", "OS Error.\n"),
                    }.get(AlarmCfg['lang'], lambda : ("錯誤", "作業系統錯誤\n"))())
            '''
            #tkmsgbox.showerror(til, txt, parent = root)
            '''
            args = [root, til, txt]
            VisualNumPad = CreateVisualKeyboard('showerror', 'VisualNumPad', args)
            VisualNumPad.focus_set()
            self.wait_window(VisualNumPad)
            '''
            showerrorFrm = GetGlobals('showerrorFrm')
            showerrorFrm.msg_var.set(txt)
            showerrorFrm.updatepos('err')
            showerrorFrm.tkraise()

    def Save4Advanced(self):
        global AlarmCfg,Opt2ActFrm,showerrorFrm
        #'Save4AdvancedSus_til = MFOGJHKGLDOELGJHOGBGMGKGLGMFKHMHAFLHGGDG'
        #'Save4AdvancedSus_txt = MFOGJHKGLDOELGJHOGBGMGKGLGMFKHMHAFLHHHLH'
        til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MFOGJHKGLDOELGJHOGBGMGKGLGMFKHMHAFLHGGDG'),
                    Config4Lan.get(AlarmCfg['lang'], 'MFOGJHKGLDOELGJHOGBGMGKGLGMFKHMHAFLHHHLH'))
        '''
        til, txt = (
            {
                'zh-TW' : lambda : ("修改確認", "確定儲存設定"),
                'en-US' : lambda : ("Confirm", "OK to save the settings"),
                }.get(AlarmCfg['lang'], lambda : ("修改確認", "確定儲存設定"))())
        '''
        args = [root, til, txt]
        VisualNumPad = CreateVisualKeyboard('askyesno', 'VisualNumPad', args)
        VisualNumPad.focus_set()
        self.wait_window(VisualNumPad)
        _check = bool(VisualNumPad.btn_var.get())
        if _check :
        #if tkmsgbox.askyesno(til, txt, parent = self):
            
            #Opt2ActFrm["00001"][2].resetData()
            resetData()

            if self.verselvar.get() >3:
                self.verselvar.set(0)
            
            db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
            db.execute("PRAGMA journal_mode=WAL")
            cursor  = db.cursor()
            cursor.execute(
                            "update alarmcfg set bee_pin = ?, yl_pin = ?, CH1_LPIN = ?,"+
                            #"Ch1_HPIN = ?, Ch2_LPIN = ?, Ch3_LPIN = ?,"+
                            #"Ch4_LPIN = ?, sync = ?, +
                            "chx_sel = ?, demo = ?," +
                            #"ver_sel = ?,
                            "loginlaw = ?, isIdlesupport = ? "+
                            "where sn = '00001'",
                            (self.gpio['bee_pin'].get(), self.gpio['yl_pin'].get(), self.beetypevar .get(),
                             #self.gpio['Ch1_LPIN'].get(), self.gpio['Ch1_HPIN'].get(), self.gpio['Ch2_LPIN'].get(), self.gpio['Ch3_LPIN'].get(),
                             #self.gpio['Ch4_LPIN'].get(), self.syncvar.get(),
                             self.chx_selvar.get(), self.demovar.get(),
                             #self.verselvar.get(),
                             self.loginlawvar.get(), self.isIdlesupportvar.get())
                            )
            #if self.chx_selvar.get() == 0:
                #cursor.execute("update group_setting set act = 1 where sn = '0'")   #如果只有一群組，強制將第 0 群設為起始群組
                
            db.commit()
            #'LangChg_til : DEOGBGIGMEHGIGAFLHGGDG'
            #'LangChg_txt : DEOGBGIGMEHGIGAFLHHHLH'
            til, txt = (Config4Lan.get(AlarmCfg['lang'], 'DEOGBGIGMEHGIGAFLHGGDG'),
                        Config4Lan.get(AlarmCfg['lang'], 'DEOGBGIGMEHGIGAFLHHHLH'))
            '''
            til, txt = (
                {
                    'zh-TW' : lambda : ("訊息", "注意！設定將於重新\n啟動後才會生效‧‧‧"),
                    'en-US' : lambda : ("Information", "Note！The setting will not\ntake effect until restarted‧‧‧"),
                    }.get(AlarmCfg['lang'], lambda : ("訊息", "注意！設定將於重新\n啟動後才會生效‧‧‧"))())
            '''
            '''
            args = [root, til, txt]
            VisualNumPad = CreateVisualKeyboard('showinfo', 'VisualNumPad', args)
            VisualNumPad.focus_set()
            self.wait_window(VisualNumPad)
            '''
            showerrorFrm = GetGlobals('showerrorFrm')
            showerrorFrm.msg_var.set(txt)
            showerrorFrm.updatepos('info')
            showerrorFrm.tkraise()
            #tkmsgbox.showwarning(til, txt, parent = self)
        pass

    def getGPIO(self, obj):
        global status,AlarmCfg,StatusBar,tilBar,Opt2ActFrm,showerrorFrm
        
        if GetGlobals('GPIOForm') is not None:
            o = obj
            if status == 0:
                UpdateOptStates(tilBar, 0)
                UpdateOptStates(StatusBar, 0)
                UpdateOptStates(self, 0)
                thisFrm = tilBar.control_variable.get()
                lKey = [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if thisFrm in x][0])][0]
                UpdateOptStates(Opt2ActFrm[lKey][2], 0)

                args = [self, o]
                VisualNumPad = CreateVisualKeyboard('GPIOForm', 'VisualNumPad', args)
                VisualNumPad.focus_set()
                #VisualNumPad.bind('<FocusOut>', lambda widget: AlarmFrm.closetoplevel(self, VisualNumPad))
            else:
                #'Stop_til : MFLHAGPHAFLHGGDG'
                #'Stop_txt : MFLHAGPHAFLHHHLH'
                til, txt = (Config4Lan.get(AlarmCfg['lang'], 'MFLHAGPHAFLHGGDG'),
                            Config4Lan.get(AlarmCfg['lang'], 'MFLHAGPHAFLHHHLH'))
                '''
                til, txt = (
                    {
                        'zh-TW' : lambda : ("訊息", "請先暫停測試\n"),
                        'en-US' : lambda : ("Information", "Please Stop First.\n"),
                        }.get(AlarmCfg['lang'], lambda : ("訊息", "請先暫停測試\n"))())
                '''
                #tkmsgbox.showerror(til, txt, parent = root)
                '''
                args = [root, til, txt]
                VisualNumPad = CreateVisualKeyboard('showerror', 'VisualNumPad', args)
                VisualNumPad.focus_set()
                self.wait_window(VisualNumPad)
                '''
                showerrorFrm = GetGlobals('showerrorFrm')
                showerrorFrm.msg_var.set(txt)
                showerrorFrm.updatepos('err')
                showerrorFrm.tkraise()
            pass
        else:
            #'PWMTestOsErr_til : PFIFCELFKGMHLHAEMHKENHNHAFLHGGDG'
            #'PWMTestOsErr_txt : PFIFCELFKGMHLHAEMHKENHNHAFLHHHLH'
            til, txt = (Config4Lan.get(AlarmCfg['lang'], 'PFIFCELFKGMHLHAEMHKENHNHAFLHGGDG'),
                        Config4Lan.get(AlarmCfg['lang'], 'PFIFCELFKGMHLHAEMHKENHNHAFLHHHLH'))
            '''
            til, txt = (
                {
                    'zh-TW' : lambda : ("錯誤", "作業系統錯誤\n"),
                    'en-US' : lambda : ("Error", "OS Error.\n"),
                    }.get(AlarmCfg['lang'], lambda : ("錯誤", "作業系統錯誤\n"))())
            '''
            #tkmsgbox.showerror(til, txt, parent = root)
            '''
            args = [root, til, txt]
            VisualNumPad = CreateVisualKeyboard('showerror', 'VisualNumPad', args)
            VisualNumPad.focus_set()
            self.wait_window(VisualNumPad)
            '''
            showerrorFrm = GetGlobals('showerrorFrm')
            showerrorFrm.msg_var.set(txt)
            showerrorFrm.updatepos('err')
            showerrorFrm.tkraise()
    
#=================================================================
#======================== usEntry ===========================
class adDoubleEntry(tk.Entry):
    def __init__(self, parent):
        global root
        tk.Entry.__init__(self, parent)
        #self.config(bd = 2, font = ('IPAGothic', 20, 'bold'), width = 15)
        self.oldfg = self.cget("background")
        self.script = None
        self.txtvar = None
#=================================================================
#========================= ADCsetting Windows ==========================
'''
class ADCSetting(tk.Toplevel):
    def __init__(self, parent, info):
        global curPath,root,AlarmCfg,comportlist,GroupSet
        tk.Toplevel.__init__(self, parent)

        size = (root.winfo_width(), root.winfo_height())
        left = root.winfo_x()
        top = root.winfo_y()
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))
 
        if thisOS == 'Windows' :
            self.resizable(width = False, height = False)    #可否變更大小

        elif thisOS == 'Linux' :
            self.attributes('-fullscreen', True)    #全螢幕
 

        self.protocol("WM_DELETE_WINDOW", self.on_exit)    #重新導向 Close Even
        #self.transient(parent)
        self.icon = tk.PhotoImage( file = (curPath +'//serial.png'))
        #self.attributes("-topmost", 1) #最上層顯示

        {
            'zh-TW' : lambda : self.title('serial port setting'),
            'en-US' : lambda : self.title('serial port setting'),
            }.get(AlarmCfg['lang'], lambda : self.title('serial port setting'))()
        self.tk.call('wm', 'iconphoto', self._w, self.icon)
        self.configure(background='#ffffff', takefocus = True, bd = 0)    #背景顏色
'''
class ADCSetting(tk.Frame):
    def __init__(self, parent, info):
        global tilBar,StatusBar,VisualNumPad
        global curPath,root,AlarmCfg,comportlist,GroupSet,chk_0_Raw,chk_1_Raw
        tk.Frame.__init__(self, parent)
        h = root.winfo_height() -StatusBar['height'] #H = 374
        self.config(relief = tk.GROOVE, bg = '#ffffff', width = root.winfo_width(), height = h)
        self.place(x = 0, y = 0)
        
        self.info = info
        #self.VisualNumPad = None
        curPath = GetGlobals('curPath')

        self.chk_0_Img = chk_0_Raw.resize((30, 30), Image.ANTIALIAS)
        self.chk_1_Img = chk_1_Raw.resize((30, 30), Image.ANTIALIAS)
        self.chk_0_Img = ImageTk.PhotoImage(self.chk_0_Img)
        self.chk_1_Img = ImageTk.PhotoImage(self.chk_1_Img)

        self.StartRec_0 = Image.open((curPath +"//en_StartRec_0.png"))
        self.StartRec_0 = self.StartRec_0.resize((90, 50), Image.ANTIALIAS)
        self.StartRec_0 = ImageTk.PhotoImage(self.StartRec_0)
        self.StartRec_1 = Image.open((curPath +"//en_StartRec_1.png"))
        self.StartRec_1 = self.StartRec_1.resize((90, 50), Image.ANTIALIAS)
        self.StartRec_1 = ImageTk.PhotoImage(self.StartRec_1)

        self.name = None
        comportlist = GetGlobals('comportlist')
        #============================ Get Parameters =====================================
        db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
        db.execute("PRAGMA journal_mode=WAL")
        cursor  = db.cursor()
        cursor.execute("select * from adc_setting where sn = ?", (self.info,))
        fnames = list(map(lambda x: x[0], cursor.description))
        res = cursor.fetchall() #取得記錄數
        db.commit()
        cursor.close()
        db.close()
        self.port = ([res[0][idx] for idx in range(len(fnames)) if fnames[idx] == 'port'][0])
        self.baudrate = ([res[0][idx] for idx in range(len(fnames)) if fnames[idx] == 'baudrate'][0])
        self.parity = ([res[0][idx] for idx in range(len(fnames)) if fnames[idx] == 'parity'][0])
        self.bytesize = ([res[0][idx] for idx in range(len(fnames)) if fnames[idx] == 'bytesize'][0])
        self.stopbits = ([res[0][idx] for idx in range(len(fnames)) if fnames[idx] == 'stopbits'][0])
        self.timeout = ([res[0][idx] for idx in range(len(fnames)) if fnames[idx] == 'timeout'][0])
        #=================================================================================
        self.BackGrdFrm = tk.Frame(self, relief = tk.FLAT,
                                     bg = self['bg'],
                                   width = root.winfo_width(), height = h)
        self.BackGrdFrm.place(x =0, y =0)
        #=================== Serial Port Configuration ========================

        self.serialset = tk.LabelFrame(self.BackGrdFrm, relief = tk.GROOVE, bg = self['bg'],
                                        text = 'Serial Port Conf.',
                                        font = ('IPAGothic', 12, 'bold'),
                                        fg = "#0000ff",
                                        height = 40, bd = 1)

        self.serialset0 = tk.Frame(self.serialset, relief = tk.FLAT,
                                   bg = self['bg'],
                                   height = 40, bd = 0)

        self.comportlistLbl = tk.Label(self.serialset0, bg = self['bg'],
                                       text = 'Port', font = ('IPAGothic', 12, 'bold'),
                                       relief = tk.FLAT,
                                       compound="center")
        #self.comportlistLbl.grid(row =0, column =0, rowspan =2, stick = tk.W+tk.E+ tk.N+ tk.S)
        self.comportlistLbl.grid(row =0, column =0, rowspan =1, stick = tk.SW)
        self.comportlistVar = tk.StringVar()
        self.comportlistOpt = tk.OptionMenu(self.serialset0, self.comportlistVar, *comportlist)
        self.comportlistOpt['menu'].config(font = ('IPAGothic',14, 'bold'))
        self.comportlistOpt.config(height = 1, font = ('IPAGothic', 14, 'bold'))
        if self.port in comportlist:
            self.comportlistVar.set(self.port)
        #self.comportlistOpt.grid(row = 0, column =1, rowspan =2, stick = tk.W+tk.E+ tk.N+ tk.S)
        self.comportlistOpt.grid(row = 0, column =1, rowspan =1, columnspan =1, stick = tk.NW)

        self.BaudRatLbl = tk.Label(self.serialset0, bg = self['bg'],
                                   text = 'BaudRate', font = ('IPAGothic', 12, 'bold'),
                                   relief = tk.FLAT,
                                   compound="center")
        #self.BaudRatLbl.grid(row = 0, column =2, columnspan =2, stick = tk.SE)
        self.BaudRatLbl.grid(row = 0, column =2, columnspan =1, stick = tk.SW)

        self.BaudRatVar = tk.IntVar()
        self.BaudRatAry =[9600, 115200, 128000, 256000]
        self.BaudRatOpt = tk.OptionMenu(self.serialset0, self.BaudRatVar, *self.BaudRatAry)
        self.BaudRatOpt.config(height = 1, font = ('IPAGothic', 14, 'bold'))
        self.BaudRatOpt['menu'].config(font = ('IPAGothic',14, 'bold'))
        #self.BaudRatOpt.grid(row = 0, column =4, columnspan =2, stick = tk.SE)
        self.BaudRatOpt.grid(row = 0, column =3, columnspan =1, stick = tk.NW)
        if self.baudrate in self.BaudRatAry:
            self.BaudRatVar.set(self.baudrate)

        self.TimeOutLbl = tk.Label(self.serialset0, bg = self['bg'],
                                   text = 'Timeout', font = ('IPAGothic', 12, 'bold'),
                                   relief = tk.FLAT,
                                   compound="center")
        #self.TimeOutLbl.grid(row = 0, column =6, columnspan =2, stick = tk.SE)
        self.TimeOutLbl.grid(row = 0, column =4, columnspan =1, stick = tk.SW)

        self.TimeOutVar = tk.DoubleVar()

        self.valcmd = (self.register(gotfocus),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        self.TimeOutOpt = adDoubleEntry(self.serialset0)
        self.TimeOutOpt.script = 'Input TimeOut'
        self.TimeOutOpt.config(textvariable = self.TimeOutVar)
        self.TimeOutOpt.config(bd = 2, font = ('IPAGothic', 14, 'bold'), width = 6)
        self.TimeOutOpt.config(validate = 'focus', validatecommand = self.valcmd)
        self.TimeOutOpt.txtvar =  self.TimeOutVar
        #self.TimeOutOpt.grid(row = 0, column =8, columnspan =2, stick = tk.SE)
        self.TimeOutOpt.grid(row = 0, column =5, columnspan =1, stick = tk.SW)

        self.TimeOutVar.set(self.timeout)

        self.serialset1 = tk.Frame(self.serialset, relief = tk.FLAT,
                                   bg = self['bg'],
                                   height = 40, bd = 0)

        self.ParityLbl = tk.Label(self.serialset1, bg = self['bg'],
                                  text = 'Parity', font = ('IPAGothic', 12, 'bold'),
                                  relief = tk.FLAT,
                                  compound="center")
        #self.ParityLbl.grid(row = 1, column =2, stick = tk.SW)
        self.ParityLbl.grid(row = 0, column =0, stick = tk.SW)

        self.ParityVar = tk.StringVar()
        self.ParityAry = ['N', 'O', 'E']
        self.ParityOpt = tk.OptionMenu(self.serialset1, self.ParityVar, *self.ParityAry)
        self.ParityOpt.config(height = 1, font = ('IPAGothic', 12, 'bold'))
        self.ParityOpt['menu'].config(font = ('IPAGothic', 12, 'bold'))
        self.ParityOpt.config(state= tk.DISABLED)
        #self.ParityOpt.grid(row = 1, column =3, stick = tk.SE)
        self.ParityOpt.grid(row = 0, column =1, stick = tk.SW)
        if self.parity in self.ParityAry :
            self.ParityVar.set(self.parity)

        self.DataByteLbl = tk.Label(self.serialset1, bg = self['bg'],
                                    text = 'ByteSize', font = ('IPAGothic', 12, 'bold'),
                                    relief = tk.FLAT,
                                    compound="center")
        #self.DataByteLbl.grid(row = 1, column =4, stick = tk.SW)
        self.DataByteLbl.grid(row = 0, column =2, stick = tk.SW)

        self.DataByteVar = tk.IntVar()
        self.DataByteAry = [7, 8]
        self.DataByteOpt = tk.OptionMenu(self.serialset1, self.DataByteVar, *self.DataByteAry)
        self.DataByteOpt.config(height = 1, font = ('IPAGothic', 12, 'bold'))
        self.DataByteOpt['menu'].config(font = ('IPAGothic', 12, 'bold'))
        self.DataByteOpt.config(state= tk.DISABLED)
        #self.DataByteOpt.grid(row = 1, column =5, stick = tk.SE)
        self.DataByteOpt.grid(row = 0, column =3, stick = tk.SW)
        if self.bytesize in self.DataByteAry:
            self.DataByteVar.set(self.bytesize)

        self.StopBitLbl = tk.Label(self.serialset1, bg = self['bg'],
                                   text = 'Stop Bit', font = ('IPAGothic', 12, 'bold'),
                                   relief = tk.FLAT,
                                   compound="center")
        #self.StopBitLbl.grid(row = 1, column =6, stick = tk.SW)
        self.StopBitLbl.grid(row = 0, column =4, stick = tk.SE)

        self.StopBitVar = tk.IntVar()
        self.StopBitAry = [1, 2]
        self.StopBitOpt = tk.OptionMenu(self.serialset1, self.StopBitVar, *self.StopBitAry)
        self.StopBitOpt.config(height = 1, font = ('IPAGothic', 12, 'bold'))
        self.StopBitOpt['menu'].config(font = ('IPAGothic', 12, 'bold'))
        self.StopBitOpt.config(state= tk.DISABLED)
        #self.StopBitOpt.grid(row = 1, column =7, stick = tk.SE)
        self.StopBitOpt.grid(row = 0, column =5, stick = tk.SW)
        if self.stopbits in self.StopBitAry:
            self.StopBitVar.set(self.stopbits)

        self.Save4ComBtn = tk.Button(self.serialset1, text='SaveCom', font = ('IPAGothic', 14, 'bold'), image = '',
                                     compound="center", command = self.Save4Com)
        self.Save4ComBtn.config(activebackground = "#dddddd", bg = '#ff0000', relief = tk.RAISED, bd = 2)
        #self.Save4ComBtn.grid(row = 1, column =8, stick = tk.SE)
        self.Save4ComBtn.grid(row = 0, column =7, stick = tk.SE)
        
        #===================================================================
        #=============================Tool Frame ===============================
        '''
        self.ToolFrm = tk.Frame(self.BackGrdFrm,
                                relief = tk.FLAT,
                                bg = self['bg'], bd =0)
        '''
        self.icon4exit = tk.PhotoImage(file = (curPath +"//Error.png"))
        self.exitbtn = tk.Button(self, image = self.icon4exit, bg = '#ffffff',
                                 relief = tk.FLAT, bd =0, command = self.on_exit)
        self.exitbtn.place(x = (self['width'] -self.exitbtn.winfo_reqwidth()),
                           y = 0)
        #self.exitbtn.grid(row = 0, column =0, columnspan =1, padx =0, stick = tk.SE)

        self.numpadicon = Image.open((curPath +"//num_key.png"))
        self.numpadicon = self.numpadicon.resize((40, 35), Image.ANTIALIAS)
        self.numpadicon = ImageTk.PhotoImage(self.numpadicon)

        self.NumPad= tk.Button(self, text='',
                               image = self.numpadicon,
                               bg ='#ffffff',
                               relief = tk.FLAT, bd =0,
                               compound="center",
                               command = self.actFltPad)
        
        self.NumPad.place(x = (self['width'] -self.NumPad.winfo_reqwidth()),
                          y = self.exitbtn.winfo_reqheight() +10)
        #self.NumPad.grid(row = 1, column =0, columnspan =1, padx =0, stick = tk.SE)

        #===================================================================
        #======================== Chart Frame ===================================
        self.ChartFrm = tk.Frame(self.BackGrdFrm,
                                 relief = tk.GROOVE, bg = self['bg'],
                                 bd = 1,
                                 height = 245,
                                 width =515)
        #================ ax4wave ==================
        self.figDpi = 72.0
        self.inifigH = 240
        self.inifigW = 455
        self.figH = self.inifigH / self.figDpi
        self.figW = self.inifigW / self.figDpi
        self.fig4main = Figure(figsize = (self.figW, self.figH), dpi = self.figDpi, facecolor = '#dddddd')#self['bg'])
        self.def_til_font = FontProperties(fname = (rawS(curPath + '//msjhbd.ttc')))

        self.otherfig = {}
        self.otherfig['wave'] = {}
        axL = ((self.figDpi / 72) / self.inifigW) *55.0
        axR = ((self.figDpi / 72) / self.inifigW) *10.0
        axB = ((self.figDpi / 72) / self.inifigH) *78.0
        axT = ((self.figDpi / 72) / self.inifigH) *20.0
        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        self.otherfig['wave']['axes'] = self.fig4main.add_axes(axSize)

        self.otherfig['wave']['lev'] = {}
        [self.otherfig['wave']['lev'].update({x : self.otherfig['wave']['axes'].plot([], [], 'r-', linewidth = 1, markersize = 1)})
         for x in [1, -1]]
        #self.otherfig['wave']['lev'] = [self.otherfig['wave']['axes'].plot([], [], 'r-', linewidth = 1, markersize = 1)
                                        #for x in [1, -1]]
        self.otherfig['wave']['path'] = [self.otherfig['wave']['axes'].plot([], [], '-', linewidth = 1, markersize = 1,
                                                                            label = 'CH %s' %x)
                                         for x in [0, 1]]

        self.otherfig['wave']['axes'].set_xlim([0, 512])
        self.otherfig['wave']['axes'].set_ylim([-1500, 1500])
        self.otherfig['wave']['xlim'] = self.otherfig['wave']['axes'].get_xlim()
        [self.otherfig['wave']['lev'][x][0].set_data(self.otherfig['wave']['xlim'], [x *0, x *0]) for x in [1, -1]]
        
        self.def_til_font = FontProperties(fname = (rawS(curPath + '//msjhbd.ttc')))
        self.def_til_font.set_size(math.ceil(10*72/self.figDpi))

        self.otherfig['wave']['axes'].legend([self.otherfig['wave']['path'][i][0] for i in range(0, len(self.otherfig['wave']['path']))],
                                             [vars(self.otherfig['wave']['path'][i][0])['_label'] for i in range(0, len(self.otherfig['wave']['path']))],
                                             loc = 2)
        
        [label.set_fontproperties(self.def_til_font) for label in self.otherfig['wave']['axes'].get_xticklabels()]
        [label.set_fontproperties(self.def_til_font) for label in self.otherfig['wave']['axes'].get_yticklabels()]
        self.def_til_font.set_size(math.ceil(12 *72/self.figDpi))
        self.def_til_font.set_weight('bold')
        self.otherfig['wave']['axes'].set_title(u'WaveForm', fontproperties = self.def_til_font, x = 0.1)
        self.def_til_font.set_size(math.ceil(12*72 /self.figDpi))
        self.def_til_font.set_weight('normal')
        self.otherfig['wave']['axes'].set_xlabel(u'Time(ns)', fontproperties = self.def_til_font, x = 0.94, y = 0)
        self.otherfig['wave']['axes'].set_ylabel(u'Amp.(mv)', fontproperties = self.def_til_font)

        #self.otherfig['wave']['axes'].set_autoscaley_on(True)
        self.otherfig['wave']['axes'].xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%d'))
        self.otherfig['wave']['axes'].yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%d'))
        self.otherfig['wave']['axes'].grid()
        self.otherfig['wave']['axes'].relim()
        self.otherfig['wave']['axes'].autoscale_view()

        #===========================================

        self.canvas4main = FigureCanvasTkAgg(self.fig4main, self.ChartFrm)
        self.canvas4main.get_tk_widget().place(x = 55, y = 0)
        self.canvas4main._tkcanvas.place(x = 55, y = 0)

        self.fig4main.canvas.draw()
        self.fig4main.canvas.flush_events()

        self.toolbar4main = CustomToolbar(self.canvas4main, self.ChartFrm)
        self.toolbar4main.config(bg = "#dddddd")
        self.toolbar4main.place(x = 55,
                                y = (self.inifigH -self.toolbar4main.winfo_reqheight() -8))
        self.toolbar4main.update()
        self.toolbar4main.tkraise()

        #====================== Trigger Lev. setting =======================
        self.Grx_trigLv = tk.IntVar()
        self.GrxTrigLvFrm = tk.Frame(self.ChartFrm, relief = tk.GROOVE,
                                     bg = self['bg'], bd = 1)
        #self.GrxTrigLvLbl = tk.Label(self.GrxTrigLvFrm, bg = self['bg'], compound="center",
                                     #font = ('IPAGothic', 10, 'bold'),
                                     #text =  'Lev.')

        self.GrxTrigMvLbl = tk.Label(self.GrxTrigLvFrm, bg = self['bg'], compound="center",
                                     fg = '#0000ff',
                                     font = ('IPAGothic', 8, 'bold'),
                                     text =  '0 mV')

        self.GrxTrigLvOpt = tk.Scale(self.GrxTrigLvFrm, label = '', from_ = 1200, to = 0,
                                     orient = tk.VERTICAL, length = self.inifigH -20, showvalue = 0,
                                     font = ('IPAGothic', 8, 'normal'),
                                     tickinterval = -200, resolution = -1,
                                     variable = self.Grx_trigLv,
                                     relief = tk.GROOVE, bd = 1,
                                     command = self.showTrigLv)
        
        #self.GrxTrigLvLbl.pack()
        self.GrxTrigLvOpt.pack()
        self.GrxTrigMvLbl.pack()
        self.GrxTrigLvFrm.place(x = 0, y = 0)

        #==================== Trigger List Frame ===============================
        self.TrigLstLrm = tk.LabelFrame(self.BackGrdFrm, relief = tk.GROOVE, bg = self['bg'],
                                        text = 'Trig. List',
                                        font = ('IPAGothic', 12, 'bold'),
                                        fg = "#0000ff", bd = 1,
                                        height = 345,
                                        width =220)

        #self.Back4TrigLst = tk.Frame(self.TrigLstLrm,
                                     #relief = tk.FLAT, bg = '#dddddd',#self['bg'],
                                     #bd = 0,
                                     #height = 240,
                                     #width = 800)
        #self.Back4TrigLst.place(x =0, y =0)
        #====================================================\
        self.adcsetbak = tk.Frame(self.BackGrdFrm,
                                  relief = tk.FLAT,
                                  bg = self['bg'], bd =0)
        #============== Get Calibration Parameters =====================
        self.CaliSet = tk.LabelFrame(self.adcsetbak,#self.BackGrdFrm,
                                     relief = tk.GROOVE, bg = self['bg'],
                                     text = 'Config_g%s.ini' %self.info,
                                     font = ('IPAGothic', 12, 'bold'),
                                     fg = "#0000ff", height = 200, width = 100, bd = 1)
        
        #self.GroupSet = GetGlobals('GroupSet')
        #self.GroupSet = {}
        #self.GroupSet[self.info]['Calib'] = {}
        self.creatNewCali = False
        self.Config4opt = ConfigLib.ConfigParser()
        self.Config4opt.optionxform = str

        if os.path.isfile((curPath + ('//config_g%s' %self.info) +'.ini')):
            try:
                self.Config4opt.read((curPath + ('//config_g%s' %self.info) +'.ini'))
                for j in [0, 1]:
                    try:
                        self.coef = self.Config4opt.getfloat('Calibration%s' %j, 'coef')
                        self.intercept = self.Config4opt.getfloat('Calibration%s' %j, 'intercept')
                        #self.GroupSet[self.info]['Calib'][j] = {'coef' : self.coef, 'intercept' : self.intercept}
                    except:
                        self.creatNewCali = True
            except:
                self.creatNewCali = True
        else:
            self.creatNewCali = True
            
        if self.creatNewCali:
            for j in [0, 1]:
                self.Config4opt.add_section('Calibration%s' %j)
                self.Config4opt.set('Calibration%s' %j, 'coef', '10.0')
                self.Config4opt.set('Calibration%s' %j, 'intercept', '-128.0')
                #self.GroupSet[i]['Calib'][j] = {'coef' : self.Config4opt.getfloat('Calibration%s' %j, 'coef'),
                                                #'intercept' : self.Config4opt.getfloat('Calibration%s' %j, 'intercept')}

        self.calitxtvar = {}
        self.caliEntry = {}
        for i in range(0, len(list(self.Config4opt.sections()))):
            _sec = list(self.Config4opt.sections())[i]
            _lblfrm = tk.LabelFrame(self.CaliSet, relief = tk.GROOVE,
                                    bg = self['bg'],
                                    fg = "#00ff00",
                                    text = '[%s]' %_sec,
                                    font = ('IPAGothic', 12, 'bold')
                                    )
            _lblfrm.grid(column = i, row =0, stick = tk.SW)
            for j in range(0, len(list(self.Config4opt.options(_sec)))):
                _opt = list(self.Config4opt.options(_sec))[j]
                tk.Label(_lblfrm, bg = self['bg'],
                         text = _opt[:5],
                         font = ('IPAGothic', 12, 'bold'),
                         relief = tk.FLAT,
                         compound = "left").grid(row = j, column =0, stick = tk.SE)

                self.calitxtvar[len(self.calitxtvar)] = tk.DoubleVar()
                self.caliEntry[len(self.caliEntry)] = adDoubleEntry(_lblfrm)
                self.caliEntry[(len(self.caliEntry) -1)].script = 'Input _g%s/%s' %(self.info, _opt)
                self.caliEntry[(len(self.caliEntry) -1)].config(textvariable = self.calitxtvar[(len(self.calitxtvar) -1)])
                self.caliEntry[(len(self.caliEntry) -1)].config(bd = 2, font = ('IPAGothic', 12, 'bold'), width = 6)
                self.caliEntry[(len(self.caliEntry) -1)].config(validate = 'focus', validatecommand = self.valcmd)
                self.caliEntry[(len(self.caliEntry) -1)].txtvar =  self.calitxtvar[(len(self.calitxtvar) -1)]
                self.calitxtvar[(len(self.calitxtvar) -1)].set(self.Config4opt.getfloat(_sec, _opt))
                self.caliEntry[(len(self.caliEntry) -1)].grid(row = j, column =1, stick = tk.NE)


        self.Save4CaliBtn = tk.Button(self.CaliSet, text='Save Calibra', font = ('IPAGothic', 12, 'bold'), image = '',
                                     compound="center", command = self.Save4Cali)
        self.Save4CaliBtn.config(activebackground = "#dddddd", bg = '#ff0000', relief = tk.RAISED, bd = 2, wraplength = 60)
        self.Save4CaliBtn.grid(column = len(list(self.Config4opt.sections())), row =0, stick = tk.SE)
        #====================================================
        #======================== FPGA setting Frame =======================

        self.adcset = tk.Frame(self.adcsetbak,
                               relief = tk.GROOVE, bg = self['bg'],
                               bd = 1,
                               height = 85)
        self.onoffswitch_var = tk.IntVar()
        self.onoffswitch = tk.Checkbutton(self.adcset, variable = self.onoffswitch_var, bd = 0,
                                          relief = tk.FLAT, image = self.StartRec_0, selectimage = self.StartRec_1)
        self.onoffswitch.config(activebackground = "#ffffff", bg = "#ffffff", indicatoron  = 0, onvalue = 1)
        self.onoffswitch.config(offvalue = 0, compound = tk.LEFT, width = 90, command = self.startRec)
        self.onoffswitch_var.set(0)
        self.onoffswitch.grid(row =0, column =3,
                              rowspan =1, columnspan =1, stick = tk.SW)

        for i in [0, 1]:
            vars(self)[('Ch%s_Conf' %i)] = tk.LabelFrame(self.adcset,
                                                         relief = tk.GROOVE, bg = self['bg'],
                                                         text = 'Ch%s' %i,
                                                         font = ('IPAGothic', 12, 'bold'),
                                                         fg = self.otherfig['wave']['path'][i][0].get_color(),#"#0000ff",
                                                         bd = 1,
                                                         height =40,
                                                         width = 100)
            
            vars(self)['Ch%s_var' %i] = tk.IntVar()
            vars(self)['Ch%s_var' %i].set(1)
            vars(self)['Ch%s_View' %i] = tk.Checkbutton(vars(self)[('Ch%s_Conf' %i)],
                                                        variable = vars(self)['Ch%s_var' %i],
                                                        bd = 0, relief = tk.FLAT,
                                                        image = self.chk_0_Img,
                                                        selectimage = self.chk_1_Img)
            vars(self)['Ch%s_View' %i].config(activebackground = "#ffffff", bg = self['bg'], indicatoron  = 0, onvalue = 1)
            vars(self)['Ch%s_View' %i].config(offvalue = 0, compound = tk.LEFT)
            vars(self)['Ch%s_View' %i].config(command = lambda ch = i: self.SetCh_View(ch))

            #========================= Ch X Gain ===============================
            self.GaintAry = {' 1x' :['1101', '1101'], '10x' :['0111', '1110'], '20x' :['1110', '0111']}
            vars(self)[('Ch%s_gain_variable' %i)] = tk.StringVar()
            vars(self)[('Ch%s_gain_variable' %i)].set(list(self.GaintAry.keys())[0])
            vars(self)[('Ch%s_gain' %i)] = tk.OptionMenu(vars(self)[('Ch%s_Conf' %i)],
                                                         vars(self)[('Ch%s_gain_variable' %i)],
                                                         *list(self.GaintAry.keys()),
                                                         command = self.commLine)
            vars(self)[('Ch%s_gain' %i)].config(font = ('IPAGothic', 14, 'bold'))
            vars(self)[('Ch%s_gain' %i)]['menu'].config(font = ('IPAGothic', 14,'bold'))

            vars(self)['Ch%s_View' %i].grid(row =0, column =0, stick = tk.NW)
            vars(self)[('Ch%s_gain' %i)].grid(row =0, column =1, stick = tk.NW)
            vars(self)[('Ch%s_Conf' %i)].grid(row =0, column =i, rowspan =1, stick = tk.NW)

        #========================= Sync select ===============================
        self.SyncAry = {'DC Input' :0, 'virtual 50Hz' :1, 'virtual 60Hz' :2}
        self.Sync_var = tk.StringVar()
        self.Sync_var.set(list(self.SyncAry.keys())[list(self.SyncAry.values()).index(0)])
        self.SyncLbl = tk.LabelFrame(self.adcset,
                                     relief = tk.GROOVE,
                                     bg = self['bg'],
                                     text = 'Sync',
                                     font = ('IPAGothic', 12, 'bold'),
                                     fg = "#0000ff",
                                     bd = 1)
        self.SyncOpt = tk.OptionMenu(self.SyncLbl, self.Sync_var,
                                     *list(self.SyncAry.keys()),
                                     command = self.commLine)
        self.SyncOpt.config(font = ('IPAGothic', 12, 'bold'))
        self.SyncOpt['menu'].config(font = ('IPAGothic',12, 'bold'))
        self.SyncOpt.config(state = tk.DISABLED)
        self.SyncOpt.pack()
        self.SyncLbl.grid(row =0, column =2,
                          rowspan =1, stick = tk.NW)
        #====================================================
        #========================= Wave select ===================
        self.Wave_var = tk.IntVar()
        self.Wave_var.set(1)
        self.Wave_check = tk.Checkbutton(self.adcset, variable = self.Wave_var,
                                         bd = 0, relief = tk.FLAT,
                                         image = self.chk_0_Img,
                                         selectimage = self.chk_1_Img,
                                         command = self.commLine)
        self.Wave_check.config(activebackground = "#ffffff", bg = self['bg'], indicatoron  = 0, onvalue = 1)
        self.Wave_check.config(offvalue = 0, compound = tk.LEFT)
        self.Wave_check.config(text = 'Wave', font = ('IPAGothic', 12, 'bold'))
        self.Wave_check.config(state = tk.DISABLED)
        self.Wave_check.grid(column = 0, row = 1,
                             rowspan = 1, columnspan = 1,
                             stick = tk.NW)
        #=====================================================
        #========================= FFT select ======================
        self.FFT_var = tk.IntVar()
        self.FFT_var.set(1)
        self.FFT_check = tk.Checkbutton(self.adcset,
                                        variable = self.FFT_var,
                                        bd = 0, relief = tk.FLAT,
                                        image = self.chk_0_Img,
                                        selectimage = self.chk_1_Img,
                                        command = self.commLine)
        self.FFT_check.config(activebackground = "#ffffff", bg = self['bg'], indicatoron  = 0, onvalue = 1)
        self.FFT_check.config(offvalue = 0, compound = tk.LEFT)
        self.FFT_check.config(text = 'FFT', font = ('IPAGothic', 12, 'bold'))
        self.FFT_check.config(state = tk.DISABLED)
        self.FFT_check.grid(column = 1, row = 1,
                            rowspan = 1, columnspan = 1,
                            stick = tk.NW)
        #=======================================================
        #======================== PRPD select ==============================
        self.PRPD_var = tk.IntVar()
        self.PRPD_var.set(1)
        self.PRPD_check = tk.Checkbutton(self.adcset,
                                         variable = self.PRPD_var,
                                         bd = 0, relief = tk.FLAT,
                                         image = self.chk_0_Img,
                                         selectimage = self.chk_1_Img,
                                         command = self.commLine)
        self.PRPD_check.config(activebackground = "#ffffff", bg = self['bg'], indicatoron  = 0, onvalue = 1)
        self.PRPD_check.config(offvalue = 0, compound = tk.LEFT)
        self.PRPD_check.config(text = 'PRPD', font = ('IPAGothic', 12, 'bold'))
        self.PRPD_check.config(state = tk.DISABLED)
        self.PRPD_check.grid(column = 2, row = 1,
                             rowspan = 1, columnspan = 1,
                             stick = tk.NW)
        #===============================================================
        #======================== TWmap select ==============================
        self.TWmap_var = tk.IntVar()
        self.TWmap_var.set(1)
        self.TWmap_check = tk.Checkbutton(self.adcset, variable = self.TWmap_var,
                                          bd = 0, relief = tk.FLAT,
                                          image = self.chk_0_Img,
                                          selectimage = self.chk_1_Img,
                                          command = self.commLine)
        self.TWmap_check.config(activebackground = "#ffffff", bg = self['bg'], indicatoron  = 0, onvalue = 1)
        self.TWmap_check.config(offvalue = 0, compound = tk.LEFT)
        self.TWmap_check.config(text = 'TWmap', font = ('IPAGothic', 12, 'bold'))
        self.TWmap_check.config(state = tk.DISABLED)
        self.TWmap_check.grid(column =3, row = 1,
                              rowspan = 1, columnspan = 1,
                              stick = tk.NW)
        '''
        self.NumPad= tk.Button(self.adcset, text='', image = self.numpadicon,
                               compound="center", command = self.actFltPad)
        
        self.NumPad.grid(column = 4, row = 1,
                         rowspan = 1, columnspan = 1,
                         stick = tk.SE)
        '''
        #===================================================================

        #self.serialset.grid(column = 0, row = 0, rowspan = 2,
                             #columnspan = 10,
                             #stick = tk.N +tk.W)

        self.serialset.grid(column = 0, row = 0, rowspan = 1,
                             columnspan = 1,
                             stick = tk.NW)

        self.serialset0.grid(column = 0, row = 0, rowspan = 1,
                             #columnspan = 12,
                             stick = tk.N +tk.W)

        self.serialset1.grid(column = 0, row = 1, rowspan = 1,
                             #columnspan = 12,
                             stick = tk.N +tk.W)

        #self.ToolFrm.grid(column = 12, row = 0,
                          #rowspan = 1,
                          #columnspan = 2,
                          #ipadx = 55,
                          #stick = tk.N +tk.E +tk.S +tk.W)

        #self.ChartFrm.grid(column = 0, row = 2, rowspan = 1,
                           #columnspan = 12,
                           #stick = tk.N +tk.W)# +tk.S +tk.W)

        self.ChartFrm.grid(column = 0, row = 1, rowspan = 1,
                           columnspan = 1,
                           stick = tk.NW)

        #self.TrigLstLrm.grid(column = 11, row = 0, rowspan = 3,
                             #columnspan = 9, padx =12,
                             #stick = tk.N +tk.W)# +tk.S +tk.W)

        self.TrigLstLrm.grid(column = 1, row = 0, rowspan = 2,
                             columnspan = 1,
                             stick = tk.NW)

        #self.CaliSet.grid(column = 10, columnspan =10, row = 3, stick = tk.N +tk.E)
        #self.adcset.grid(column = 0, columnspan =10, row = 3, stick = tk.NW)
        self.CaliSet.grid(column = 1, columnspan =1, row = 0, stick = tk.NW)
        self.adcset.grid(column = 0, columnspan =1, row = 0, stick = tk.NW)
        self.adcsetbak.grid(column = 0, columnspan =2, row = 2, stick = tk.NW)

    def startRec(self):
        pass

    def commLine(self):
        pass

    def SetCh_View(self, ch):
        pass

    def showTrigLv(self, value):
        #self.commLine(value)
        [self.otherfig['wave']['lev'][x][0].set_ydata([x *self.Grx_trigLv.get(), x *self.Grx_trigLv.get()]) for x in [1, -1]]
        self.fig4main.canvas.draw()
        self.GrxTrigMvLbl.config(text = ('%s mV' %value))
        
    def Save4Com(self):
        pass

    def Save4Cali(self):
        pass

    def actFltPad(self):
        global subClass,subform,ActInputObj,AlarmCfg,Opt2ActFrm,VisualNumPad
        ActInputObj = GetGlobals('ActInputObj')
        subform = GetGlobals('subform')
        if type(ActInputObj) == subform.adDoubleEntry:
            obj = ActInputObj.txtvar
            text = ActInputObj .script

            #try:
                #self.VisualNumPad.destroy()
            #except:
                #pass
        
            #self.VisualNumPad = VisualFltKeyboard(self, obj, text)
            args = [self, obj, text,]
            self.VisualNumPad = CreateVisualKeyboard('VisualFltKeyboard', 'VisualNumPad', args)
            self.VisualNumPad.focus_set()
            #self.VisualNumPad.bind('<FocusOut>', lambda widget: self.closetoplevel(self.VisualNumPad))
        else:
            #tkmsgbox.showerror("Information", "Please Select First.", parent = self)
            '''
            args = [root, "Information", "Please Select First.\n"]
            VisualNumPad = CreateVisualKeyboard('showerror', 'VisualNumPad', args)
            VisualNumPad.focus_set()
            self.wait_window(VisualNumPad)
            '''
            global showerrorFrm
            showerrorFrm = GetGlobals('showerrorFrm')
            showerrorFrm.msg_var.set("Please Select First.\n")
            showerrorFrm.updatepos('err')
            showerrorFrm.tkraise()

    def closetoplevel(self, widget):
        widget.destroy()

    def setPort(self, port):
        self.comportlistVar.set(port)

    def on_exit(self):
        PopGlobals(self.name)
        self.destroy()
#=================================================================
#======================= Customer Toobar ===============================
class CustomToolbar(NavigationToolbar2TkAgg):
    def __init__(self,canvas_,parent_):
        global AlarmCfg,Config4Lan
        
        self.parent = parent_
        self.disp_optObj = {}

        global curPath,AlarmCfg
        if type(self.parent) == MainFrm2:
            if os.path.isfile((os.path.join(curPath, 'images', 'disp_opt0.png'))):
                self.chk_0_Img = tk.PhotoImage(file = (os.path.join(curPath, 'images', 'disp_opt0.png')))
            elif os.path.isfile((os.path.join(matplotlib.rcParams['datapath'], 'images', 'disp_opt0.png'))):
                self.chk_0_Img = tk.PhotoImage(file = (os.path.join(matplotlib.rcParams['datapath'], 'images', 'disp_opt0.png')))
            else:
                self.chk_0_Img = tk.PhotoImage(file = None)
                
            if os.path.isfile((os.path.join(curPath, 'images', 'disp_opt1.png'))):
                self.chk_1_Img = tk.PhotoImage(file = (os.path.join(curPath, 'images', 'disp_opt1.png')))
            elif os.path.isfile((os.path.join(matplotlib.rcParams['datapath'], 'images', 'disp_opt1.png'))):
                self.chk_1_Img = tk.PhotoImage(file = (os.path.join(matplotlib.rcParams['datapath'], 'images', 'disp_opt1.png')))
            else:
                self.chk_1_Img = tk.PhotoImage(file = None)

            #self.chk_0_Img = self.chk_0_Img.zoom(2, 2)
            #self.chk_1_Img = self.chk_1_Img.zoom(2, 2)
                
            #(show text, tooltip, IMAGE, command)
            self.toolitems = (
                ('Home', Config4Lan.get(AlarmCfg['lang'], 'Home'), 'home', 'home'),
                #('Back', Config4Lan.get(AlarmCfg['lang'], 'Back'), 'back', 'back'),
                #('Forward', Config4Lan.get(AlarmCfg['lang'], 'Forward'), 'forward', 'forward'),
                ('Pan', Config4Lan.get(AlarmCfg['lang'], 'Pan'), 'move', 'pan'),
                ('Zoom', Config4Lan.get(AlarmCfg['lang'], 'Zoom'), 'zoom_to_rect', 'zoom'),
                ('disp_opt', Config4Lan.get(AlarmCfg['lang'], 'disp_opt'), 'disp_opt0', 'disp_opt'),
                )
            '''
            self.toolitems = {
                'zh-TW' : lambda : (
                    ('Home', '首頁', 'home', 'home'),
                    ('Back', '前一視圖', 'back', 'back'),
                    ('Forward', '後一視圖', 'forward', 'forward'),
                    #(None, None, None, None),
                    ('Pan', '位移', 'move', 'pan'),
                    ('Zoom', '縮放', 'zoom_to_rect', 'zoom'),
                    #(None, None, None, None),
                    #(None, None, None, None),
                    (None, None, None, None),
                    ('disp_opt', '顯示切換', 'disp_opt0', 'disp_opt'),
                    ),
            'en-US' : lambda : (
                ('Home', 'Reset original view', 'home', 'home'),
                ('Back', 'Back to previous view', 'back', 'back'),
                ('Forward', 'Fordward to next view', 'forward', 'forward'),
                #(None, None, None, None),
                ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
                ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
                #(None, None, None, None),
                #(None, None, None, None),
                (None, None, None, None),
                ('disp_opt', 'Display switching', 'disp_opt0', 'disp_opt'),
                ),
            }.get(AlarmCfg['lang'], lambda : (
                ('Home', '首頁', 'home', 'home'),
                ('Back', '前一視圖', 'back', 'back'),
                ('Forward', '後一視圖', 'forward', 'forward'),
                #(None, None, None, None),
                ('Pan', '位移', 'move', 'pan'),
                ('Zoom', '縮放', 'zoom_to_rect', 'zoom'),
                #(None, None, None, None),
                #(None, None, None, None),
                (None, None, None, None),
                ('disp_opt', '顯示切換', 'disp_opt0', 'disp_opt'),
                ))()
            '''
        else:
            self.toolitems = (
                ('Home', Config4Lan.get(AlarmCfg['lang'], 'Home'), 'home', 'home'),
                #('Back', Config4Lan.get(AlarmCfg['lang'], 'Back'), 'back', 'back'),
                #('Forward', Config4Lan.get(AlarmCfg['lang'], 'Forward'), 'forward', 'forward'),
                ('Pan', Config4Lan.get(AlarmCfg['lang'], 'Pan'), 'move', 'pan'),
                ('Zoom', Config4Lan.get(AlarmCfg['lang'], 'Zoom'), 'zoom_to_rect', 'zoom'),
                )
            '''
            self.toolitems = {
                'zh-TW' : lambda : (
                    ('Home', '首頁', 'home', 'home'),
                    ('Back', '前一視圖', 'back', 'back'),
                    ('Forward', '後一視圖', 'forward', 'forward'),
                    #(None, None, None, None),
                    ('Pan', '位移', 'move', 'pan'),
                    ('Zoom', '縮放', 'zoom_to_rect', 'zoom'),
                    #(None, None, None, None),
                    #(None, None, None, None),
                    #(None, None, None, None),
                    ),
            'en-US' : lambda : (
                ('Home', 'Reset original view', 'home', 'home'),
                ('Back', 'Back to previous view', 'back', 'back'),
                ('Forward', 'Fordward to next view', 'forward', 'forward'),
                #(None, None, None, None),
                ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
                ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
                #(None, None, None, None),
                #(None, None, None, None),
                #(None, None, None, None),
                ),
            }.get(AlarmCfg['lang'], lambda : (
                ('Home', '首頁', 'home', 'home'),
                ('Back', '前一視圖', 'back', 'back'),
                ('Forward', '後一視圖', 'forward', 'forward'),
                #(None, None, None, None),
                ('Pan', '位移', 'move', 'pan'),
                ('Zoom', '縮放', 'zoom_to_rect', 'zoom'),
                #(None, None, None, None),
                #(None, None, None, None),
                #(None, None, None, None),
                ))()
            '''

        NavigationToolbar2TkAgg.__init__(self,canvas_,parent_)

    def disp_opt(self):
        global curPath,disp_var,root
        dirc = os.path.dirname(self.disp_optObj['im'])
        file = os.path.basename(self.disp_optObj['im'])
        file, _ext = os.path.splitext(os.path.basename(file))

        _v = {
            0 : lambda : 1,
            }.get(disp_var.get(), lambda : 0)()
        
        disp_var.set(_v)
        
        file = file[0:-1] +str(_v)
        img_file = os.path.join(dirc, file + _ext)
        self.parent.display_opt()
        
    def _Button(self, text, file, command, extension = '.png'):
        global curPath,disp_var
        #img_file = os.path.join(matplotlib.rcParams['datapath'], 'images', file + extension)
        #img_file = os.path.join(curPath, 'images', file + extension)
        if os.path.isfile((os.path.join(curPath, 'images', file + extension))):
            img_file = os.path.join(curPath, 'images', file + extension)
        elif os.path.isfile((os.path.join(matplotlib.rcParams['datapath'], 'images', file + extension))):
            img_file = os.path.join(matplotlib.rcParams['datapath'], 'images', file + extension)
        else:
            img_file = None

        if command == self.disp_opt:
            b = tk.Checkbutton(self, variable = disp_var, bd = 2,
                               relief = tk.RAISED, image = self.chk_0_Img,
                               selectimage = self.chk_1_Img)
            b.config(activebackground = "#ffffff", bg = "#ffffff", indicatoron  = 0,
                     onvalue = 1, offvalue = 0, command = self.parent.display_opt)
        else:
            if img_file != None:
                im = tk.PhotoImage(master = self, file = img_file)
                # Do stuff with im here
                #im = im.zoom(2, 2)
                b = tk.Button(
                    master = self, text = text, padx = 2, pady = 2, image = im, command = command)
                b._ntimage = im
            else:
                b = tk.Button(
                    master = self, text = text, padx = 2, pady = 2, command = command)
        b.pack(side = tk.LEFT)

        return b
#=================================================================
def CreateCalabration():
    global curPath,GroupSet#,trig_chAry
    global gainDict,gainCali
    #trig_chAry = GetGlobals('trig_chAry')
    GroupSet = GetGlobals('GroupSet')
    gainDict = GetGlobals('gainDict')
    gainCali = GetGlobals('gainCali')
    
    for i in GroupSet:
        GroupSet[i]['Calib'] = {}
        creatNewCali = False
        Config4opt = ConfigLib.ConfigParser()
        Config4opt.optionxform = str
        
        if os.path.isfile((curPath + ('//config_g%s' %i) +'.ini')):
            try:
                Config4opt.read((curPath + ('//config_g%s' %i) +'.ini'))
                for j in [0, 1]:
                    GroupSet[i]['Calib'][j] = {'coef' : {}, 'intercept' : {}}
                    for key in gainDict.keys():
                        _k = key.strip()
                        try:
                            vars()['coef_%s' %_k] = Config4opt.getfloat('Calibration%s' %j, 'coef_%s' %_k)
                            vars()['intercept_%s' %_k] = Config4opt.getfloat('Calibration%s' %j, 'intercept_%s' %_k)
                            #GroupSet[i]['Calib'][j] = {'coef' : coef, 'intercept' : intercept}
                            GroupSet[i]['Calib'][j]['coef'].update({_k : vars()['coef_%s' %_k]})
                            GroupSet[i]['Calib'][j]['intercept'].update({_k : vars()['intercept_%s' %_k]})
                        except:
                            creatNewCali = True
            except:
                creatNewCali = True
        else:
            creatNewCali = True
            
        if creatNewCali:
            del Config4opt
            Config4opt = ConfigLib.ConfigParser()
            Config4opt.optionxform = str
            for j in [0, 1]:
                Config4opt.add_section('Calibration%s' %j)
                GroupSet[i]['Calib'][j] = {'coef' : {}, 'intercept' : {}}
                for key in gainDict.keys():
                    _k = key.strip()
                    Config4opt.set('Calibration%s' %j, 'coef_%s' %_k, str(gainCali[_k][0]))
                    Config4opt.set('Calibration%s' %j, 'intercept_%s' %_k, str(gainCali[_k][1]))
                    #GroupSet[i]['Calib'][j] = {'coef' : Config4opt.getfloat('Calibration%s' %j, 'coef'),
                                               #'intercept' : Config4opt.getfloat('Calibration%s' %j, 'intercept')}
                    GroupSet[i]['Calib'][j]['coef'].update({_k : gainCali[_k][0]})
                    GroupSet[i]['Calib'][j]['intercept'].update({_k : gainCali[_k][1]})

            inif = open((curPath + ('//config_g%s' %i) +'.ini'), "w")
            Config4opt.write(inif)
            inif.close()
        '''
        {0: {'coef': {'1x': 60.0, '10x': 15.0, '20x': 10.0}, 'intercept': {'1x': -128.0, '10x': -128.0, '20x': -128.0}},
         1: {'coef': {'1x': 60.0, '10x': 15.0, '20x': 10.0}, 'intercept': {'1x': -128.0, '10x': -128.0, '20x': -128.0}}}
        '''
        '''
        idx = [_i for _i in range(0, len(trig_chAry)) if trig_chAry[_i] ==GroupSet[i]['trig_ch']][0]
        GroupSet[i]['cmdline'] = bytearray([
            GroupSet[i]['trig_ch'],
            int((GroupSet[i]['trig_lv'] +GroupSet[i]['Calib'][idx]['intercept']) /GroupSet[i]['Calib'][idx]['coef']),
            GroupSet[i]['wave_out'],
            GroupSet[i]['fft_out'],
            GroupSet[i]['prpd_out'],
            GroupSet[i]['twmap_out'],
            GroupSet[i]['sync_opt'],
            GroupSet[i]['list_choose'],
            GroupSet[i]['gain']
            ])
        del idx
        print(GroupSet[i]['cmdline'])
        '''
        del Config4opt
#=============================================
#======= convGri2Grp =============================
def convGri2Grp(gri, chx):
    global StatusBar,GroupSet
    StatusBar = GetGlobals('StatusBar')
    GroupSet = GetGlobals('GroupSet')
    j = 0
    _ch = []
    _grpA = []
    while j < len(chx):
        k = 0
        _ch.append([])
        while k < (len(GroupSet[gri]['ch']) -AlarmCfg['chx_sel']):  #自動轉換單/雙通道，單通道時要分開拿取回傳直
            _ch[j].append(chx[k +j])
            k = k+1
            if (k +j) >= len(chx):
                break
        j = j +len(_ch[j])

    for _c in _ch:
        try:
            _grp = [key for key in list(StatusBar.showgrouplnk.keys()) if StatusBar.showgrouplnk[key][0] == gri and StatusBar.showgrouplnk[key][2] == _c][0]
        except:
            try:
                _grp = [key for key in list(StatusBar.showgrouplnk.keys()) if StatusBar.showgrouplnk[key][0] == gri and all([item in StatusBar.showgrouplnk[key][2] for item in _c])][0]
            except:
                _grp = None

        if _grp != None:
            _grpA.append(_grp)
            
    return _grpA
#==============================================
#=============== 合併各通道放電訊號 ================
#=========== Get Serial DATA Test Code===============
class TransADConv (threading.Thread):
    def __init__(self, threadID, name, stopper, gr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        #self.event = event
        self.stopper = stopper
        self.gr = gr
        self.in_bin = None
        self.isSuccessful = None
        self.cmdfp = None

        self.gainary = [('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][:4],
                        ('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][-4:]]

    def run(self):
        global root,GroupSet,Opt2ActFrm,FileCount
        global AlarmCfg,coef,intercept,curPath,BlandFrm
        global trig_chAry,gainDict,gainCali,status,StatusBar
        global FileLock,outpath,GroupSet,wait4reboot
        trig_chAry = GetGlobals('trig_chAry')
        gainDict = GetGlobals('gainDict')
        gainCali = GetGlobals('gainCali')
        status = GetGlobals('status')
        StatusBar = GetGlobals('StatusBar')
        outpath = GetGlobals('outpath')
        GroupSet = GetGlobals('GroupSet')

        #root.isSuccessful = None
        BlandFrm = GetGlobals('BlandFrm')

        #lKey = {
            #'zh-TW' : lambda : [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if '警 報  設 定' in x][0])][0],
            #'en-US' : lambda : [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if 'AlarmFrm2' in x][0])][0],
            #}.get(AlarmCfg['lang'], lambda : [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if '警 報  設 定' in x][0])][0])()
        '''
        if StatusBar.refreshIdlefun is not None:
            StatusBar.after_cancel(StatusBar.refreshIdlefun)
            StatusBar.refreshIdlefun = None
        '''
        for i in [self.gr]:#GroupSet:

            ##f = open((curPath +('//cmdline_g%s.~' %i)), 'rb+')
            ##GroupSet[i]['cmdfp'] = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_READ)
            
            if AlarmCfg['demo'] != 99:
            #if AlarmCfg['demo'] not in [98, 99]:
                BlandFrm.waitproc.set('Group %s' %i +' Opening......')
                GroupSet[i]['ser'] = serial.Serial()
                GroupSet[i]['ser'].port = GroupSet[i]['port']
                #root.waitproc.set('%s Opening......' %GroupSet[i]['ser'].name)
                GroupSet[i]['ser'].baudrate = GroupSet[i]['baudrate']
                GroupSet[i]['ser'].parity = GroupSet[i]['parity']
                GroupSet[i]['ser'].stopbits = GroupSet[i]['stopbits']
                GroupSet[i]['ser'].bytesize  = GroupSet[i]['bytesize']
                GroupSet[i]['ser'].timeout = GroupSet[i]['timeout']
                while not GroupSet[i]['ser'].is_open:
                    GroupSet[i]['ser'].open()
                print(GroupSet[i]['ser'], 'Open successfully.', 'cmdLine:', GroupSet[i]['cmdfp'][:])
                
            else:
                #root.waitproc.set('Group %s' %i +' Opening......')
                BlandFrm.waitproc.set('Group %s' %i +' Opening......')
                if 'pddsample' not in vars(self) or 'nbyte' not in vars(self):
                    self.pddsample = {}
                    self.nbyte = 3170
        
                try:
                    _f = open((curPath +'//sample' +('_g%s' %i)), "rb")
                    #self.pddsample[i] = _f
                    self.pddsample.update({i : _f})
                    #print(self.pddsample[i].name, 'Open successfully.')
                    
                except:
                    #print('Group %s' %i + ' open file error!')
                    #root.waitproc.set('Group %s' %i + ' open file error!')
                    BlandFrm.waitproc.set('Group %s' %i +' open file error!')
                    

                
        while self.stopper:# and not self.event.wait(GroupSet[i]['timeout']):
            #root.isSuccessful = 1
            self.isSuccessful = status
            GroupSet = GetGlobals('GroupSet')
            wait4reboot = GetGlobals('wait4reboot')
            
            for i in [self.gr]:#GroupSet:
                
                if not self.stopper:
                    break
                
                if self.cmdfp != GroupSet[i]['cmdfp'][:]:
                    self.cmdfp = GroupSet[i]['cmdfp'][:]
                
                self.trigtime = time.time()
                if AlarmCfg['demo'] != 99:
                #if AlarmCfg['demo'] not in [98 ,99]:
                    if GroupSet[i]['ser'].is_open:
                        try:
                            GroupSet[i]['ser'].reset_input_buffer()
                            GroupSet[i]['ser'].reset_output_buffer()
                            GroupSet[i]['ser'].write(bytearray(GroupSet[i]['cmdfp'][:]))
                            #print(len(GroupSet[i]['cmdline']))
                            #GroupSet[i]['ser'].write(GroupSet[i]['cmdline'])
                            #self.in_bin = GroupSet[i]['ser'].read(3127)
                            self.in_bin = GroupSet[i]['ser'].readall()
                        except:
                            self.in_bin = []
                    else:
                        self.in_bin = []
                else:
                    ns = random.randint(0, int(os.stat(self.pddsample[i].name).st_size /self.nbyte)) *self.nbyte
                    self.pddsample[i].seek(ns)
                    self.in_bin = self.pddsample[i].read(self.nbyte)

                global VisualNumPad,subClass,subclass4all
                VisualNumPad = GetGlobals('VisualNumPad')   #<class 'subclass4all.TrigLst'>

                if VisualNumPad is not None:
                    try:
                        if VisualNumPad.ObjID == 'TrigLst':
                            self.log = ('%s || len:%s\n'
                                        %(datetime.datetime.fromtimestamp(self.trigtime).strftime('%Y/%m/%d %H:%M:%S'), len(self.in_bin)))
                            VisualNumPad.triglist.config(state = tk.NORMAL)
                            VisualNumPad.triglist.insert("end", self.log)
                            VisualNumPad.triglist.see('end')
                            VisualNumPad.triglist.config(state = tk.DISABLED)
                            VisualNumPad.triglist.update()
                    except:
                        #print(self.log)
                        pass

                else:
                    #print(self.log)
                    pass

                dlen_chk = {
                    #98 : lambda : (len(self.in_bin) >=self.nbyte),
                    99 : lambda : (len(self.in_bin) >=self.nbyte)
                    }.get(AlarmCfg['demo'], lambda : (len(self.in_bin) >=3127))()

                #========================================虛擬放電=================================================
                '''
                if AlarmCfg['demo'] == 98:
                    if not dlen_chk and len(wait4reboot) >= 2:
                        if 'pddsample' not in vars(self) or 'nbyte' not in vars(self):
                            self.pddsample = {}
                            self.nbyte = 3170
                            
                        try:
                            self.pddsample[i]
                        except:
                            _f = open((curPath +'//sample' +('_g%s' %i)), "rb")
                            self.pddsample.update({i : _f})
                            
                        while not dlen_chk:
                            ns = random.randint(0, int(os.stat(self.pddsample[i].name).st_size /self.nbyte)) *self.nbyte
                            self.pddsample[i].seek(ns)
                            self.in_bin = self.pddsample[i].read(self.nbyte)
                            dlen_chk = (len(self.in_bin) >=self.nbyte)
                            #print('dlen_chk:', dlen_chk)
                    '''
                #====================================================================================================

                #if len(self.in_bin) >=3127:
                if dlen_chk:
                    if AlarmCfg['demo'] == 99:
                        self.in_bin = self.in_bin[33:3160]
                        time.sleep(random.uniform(0.0, 1.0))
                    #elif AlarmCfg['demo'] == 98:
                        #self.in_bin = self.in_bin[33:3160]
                        #time.sleep(random.uniform(0.0, 5.0))

                    self.triglist = [self.trigtime, GroupSet[i]['cmdline'], self.in_bin[:3127]]

                    FileLock = GetGlobals('FileLock')
                    _t0 = time.time()
                    while FileLock:
                        time.sleep(0.5)
                        FileLock = GetGlobals('FileLock')
                        if ((not FileLock) or ((time.time() -_t0) > 2.0)):
                            break
                    del _t0

                    if not FileLock:
                        FileLock = True
                        self.splitpdd()
                        FileLock = False
                        UpdateGlobals('FileLock', FileLock)
                    
                else:
                    if AlarmCfg['demo'] != 99:
                    #if AlarmCfg['demo'] not in [98, 99]:
                        if GroupSet[i]['ser'].is_open:
                            try:
                                GroupSet[i]['ser'].reset_input_buffer()
                                GroupSet[i]['ser'].reset_output_buffer()
                            except:
                                pass
                    else:
                        time.sleep(random.uniform(0.0, 1.0))
                        pass
                    
                if not self.stopper:
                    break

            if not self.stopper:
                break
        '''
        if StatusBar.refreshIdlefun is not None:
            StatusBar.after_cancel(StatusBar.refreshIdlefun)
            StatusBar.refreshIdlefun = None
        '''

        for i in [self.gr]:#GroupSet:
            if AlarmCfg['demo'] != 99:
            #if AlarmCfg['demo'] not in [98, 99]:
                BlandFrm.waitproc.set(GroupSet[i]['port'] +' Closing......')
                #root.waitproc.set(GroupSet[i]['port'] +' Closeding......')
                GroupSet[i]['ser'].reset_input_buffer()
                GroupSet[i]['ser'].reset_output_buffer()
                ##GroupSet[i]['cmdfp'].close()
                while GroupSet[i]['ser'].is_open:
                    GroupSet[i]['ser'].close()
                    
                #print(GroupSet[i]['port'], 'Closed successfully.')
                #root.waitproc.set(GroupSet[i]['port'] +'Closed successfully.')

            else:
                BlandFrm.waitproc.set('Group %s' %i +' Closing......')
                #root.waitproc.set('Group %s' %i +' Closeding......')
                '''
                #模擬OFF時waiting畫面停滯，造成UI當機
                _st = time.time()
                _et = time.time()
                while (_et -_st) <= 140.0:
                    _et = time.time()
                    #print(_st, _et)
                    pass
                '''
                time.sleep(1.0)
                ##GroupSet[i]['cmdfp'].close()
                self.pddsample[i].close()

        #root.isSuccessful = 0
        status = GetGlobals('status')
        self.isSuccessful = status
        del self.in_bin

    def splitpdd(self):
        global curPath,outpath,isMount,linux_user,GroupSet,AlarmCfg
        curPath = GetGlobals('curPath')
        outpath = GetGlobals('outpath')
        isMount = GetGlobals('isMount')
        linux_user = GetGlobals('linux_user')
        GroupSet = GetGlobals('GroupSet')

        #=============================================================================================
        _alt_gr = [j for j in range(0, len(GroupSet[self.gr]['ch']))
                   if ((GroupSet[self.gr]['chxpds'][j] >AlarmCfg['maxpoint']) and (GroupSet[self.gr]['chxdurat'][j] >AlarmCfg['maxdurat']))]    #[0, 1], [0], [1]
        if len(_alt_gr) >int(not(AlarmCfg['chx_sel'])): #告警等級 #雙通道時 len(_alt_gr) == 2，單通道時 len(_alt_gr) == 1
            rst_gr = []
            _grpA = convGri2Grp(self.gr, _alt_gr)
            for _grp in _grpA:  #雙通道時 len(_grpA) == 1，單通道時 len(_grpA) == 1 or 2
                rst_gr.append(_grp)
            resetData(rst_gr)
        #=============================================================================================
        
        self.lasttimepoint = int((math.ceil(time.time()/(AlarmCfg['TimeInv'] *60))) *AlarmCfg['TimeInv'] *60)      #最新時間點
        
        self.cmdline = self.triglist[1]
        self.wave_bin = self.triglist[2][:1026]
        self.fft_bin = self.triglist[2][1026:3078]
        self.prpd_bin = self.triglist[2][3078:3098]
        self.twmp_bin = self.triglist[2][3098:3117]
        self.fft_bin = [getSignInt(int.from_bytes(self.fft_bin[_i :(_i +4)], byteorder = 'big')) /100.0 for _i in range(4, len(self.fft_bin), 4)]

        self.calib = []
        for key in GroupSet[self.gr]['mmap'].keys():
            vars(self)['_%s' %key] = [] #產生self._durat, self._prpd, self._twmap, self._wave, self._fft

        _doublechk = {'check' : 0 ,'trigtime' : None}
        Col_i = None
        _t = False
        #_ColAry = [65535.0 for _ci in range(0, len(GroupSet[self.gr]['ch']))]
        #_pr_xAry = [65535.0 for _ci in range(0, len(GroupSet[self.gr]['ch']))]
        #_pr_yAry = [65535.0 for _ci in range(0, len(GroupSet[self.gr]['ch']))]

        #print(gainDict, self.gainary)   #{' 1x': ['1101', '1101'], '10x': ['0111', '1110'], '20x': ['1110', '0111']} ['0111', '1110']
        _GroupSet = {}
        for j in range(0, len(GroupSet[self.gr]['ch'])):
            _GroupSet.update({'data4wave' : { j: {'x' : [],#list(range(0, 512)),
                                                  'y': []}},
                              'data4fft' : { j: {'x' : [],#[j / (512 *0.008) for j in range(0, 256)],
                                                 'y': []}},
                              'data4main' : { j: {'x' :[], 'y': []}},
                              'data4twmp' : { j: {'x' :[], 'y': []}},
                              'maxA' : {j:[]},
                              'maxF' : {j:[]}
                              })
            try:
                _g = [_key for _key in gainDict if gainDict[_key][j] == self.gainary[j]][0]
            except Exception as e:
                #exc_type, exc_obj, exc_tb = sys.exc_info()
                #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                #print(exc_type, fname, exc_tb.tb_lineno)
                _g = '10x'

            _ig = int(_g[:2])
            _g = _g.strip()

            coef = GroupSet[self.gr]['Calib'][j]['coef'][_g]
            self.calib.append(coef)
            intercept = GroupSet[self.gr]['Calib'][j]['intercept'][_g]
            self.calib.append(intercept)

            #_pr_y = ((getSignInt(int.from_bytes(self.prpd_bin[(8 +(j *8)) :(12 +(j *8))], byteorder = 'big')) +intercept) * coef)
            _pr_y = getSignInt(int.from_bytes(self.prpd_bin[(8 +(j *8)) :(12 +(j *8))], byteorder = 'big'))
            _pr_x = getSignInt(int.from_bytes(self.prpd_bin[(4 +(j *8)) :(8 +(j *8))], byteorder = 'big'))
            #print(j, _pr_x, _pr_y)
            #if ((_pr_x != 65535.0) and (abs(_pr_y) <= ((1200.0 +intercept) * coef))):
            #if _pr_x != 65535.0 and _pr_y != 65535.0:

            if _pr_x >=0.0 and _pr_x < 360.0:
                #_pr_x = (_pr_x %360.0)  #修復phase值
                #_pr_y = (_pr_y +intercept) *coef
                _pr_y = (_pr_y *coef) +intercept
                if (AlarmCfg['demo'] ==95):
                    if (trig_chAry[j] != GroupSet[self.gr]['trig_ch']):  #DEMO箱用且非觸發通道
                        _t = ((random.randint(1, 3) %3) ==0)
                    else:
                        _t = True
                        pass
                elif (AlarmCfg['demo'] ==99):
                #elif (AlarmCfg['demo'] in [98, 99]):
                    _t0 = int((abs(_pr_y) >= GroupSet[self.gr]['trig_lv'])) #確認資料庫資料有>= Trig.Lev

                    if (trig_chAry[j] != GroupSet[self.gr]['trig_ch']):
                        _t1 = int((random.randint(1, 3) %3) ==0)
                    else:
                        _t1 = 1
                    _t = bool(_t0 *_t1)

                    #_chx = int(GroupSet[self.gr]['ch'][j])
                    #_t = int((random.randint(1, _chx) %2) ==0)
                    #_t0 = int((random.randint(1, len(GroupSet)) %len(GroupSet)) ==0)
                    #_t0 = int((random.randint(1, 2) %2) ==0)
                    '''
                    _t0 = 1
                        
                    if trig_chAry[j] != GroupSet[self.gr]['trig_ch']:
                        _t1 = int((random.randint(1, 3) %3) ==0)
                    else:
                        _t1 = 1
                    _t = bool(_t0 *_t1)
                    '''
                    #_t = True
                else:
                    _t = True
            else:
                _t = False	#未觸發

            _chksum = False
            if _t:
                _pr_y = _pr_y /_ig

                Col_i = math.ceil(_pr_x / AlarmCfg['Col_Range']) *AlarmCfg['Col_Range'] #取觸發通道的相位角
                
                if (trig_chAry[j] == GroupSet[self.gr]['trig_ch']):
                    _doublechk['trigtime'] = Col_i
                    _dl = self.triglist[0]
                    _dt = (GroupSet[self.gr]['lasttime'][len(GroupSet[self.gr]['ch'])]
                           -GroupSet[self.gr]['inittime'][len(GroupSet[self.gr]['ch'])])
                    _dt = round(_dt, 2)
                    _ds = GroupSet[self.gr]['chxpds'][len(GroupSet[self.gr]['ch'])] +1

                try:
                    if GroupSet[self.gr]['isfilter']:
                        #============ highpass ===================
                        #sfb, sfa = signal.butter(4, [0.90, 0.95], 'bandpass')
                        #sfb, sfa = signal.butter(1, [0.52, 0.60], 'bandpass')
                        #sfb, sfa = signal.butter(1, 0.24, 'lowpass')
                        sfb, sfa = signal.butter(4, 0.9, 'highpass')
                        
                        _preFA = [(float(self.wave_bin[i] *coef) +intercept) /_ig for i in range(2 +(j*512), 514 +(j*512))]
                        _GroupSet['data4wave'][j]['y'] = signal.filtfilt(sfb, sfa, _preFA)
                        #=======================================
                    else:
                        _GroupSet['data4wave'][j]['y'] = [((float(self.wave_bin[i]) *coef) +intercept) /_ig for i in range(2 +(j*512), 514 +(j*512))]

                    _GroupSet['data4wave'][j]['x'] = list(range(0, len(_GroupSet['data4wave'][j]['y'])))

       
                    _tw_x = getSignInt(int.from_bytes(self.twmp_bin[(3 +(j *8)) :(7 +(j *8))], byteorder = 'big'))
                    _tw_y = getSignInt(int.from_bytes(self.twmp_bin[(7 +(j *8)) :(11 +(j *8))], byteorder = 'big'))

                    #==== 求最大振福與頻率 ============================================================
                    _maxAar = sorted(_GroupSet['data4wave'][j]['y'], reverse = True)
                    #_maxA = sum(_maxAar[0:3])/3    #如果是效正訊號，會被平均值影響
                    _GroupSet['maxA'][j].append(_maxAar[0])
                    
                    _fy = sorted(_GroupSet['data4fft'][j]['y'], reverse = True)
                    idx = 0
                    while idx == 0:
                        try:
                            idx = [_idx for _idx in range(0, len(_GroupSet['data4fft'][j]['y'])) if _GroupSet['data4fft'][j]['y'][_idx] == _fy[0]][0]
                            _fy.pop(0)
                            if _GroupSet['data4fft'][j]['x'][idx] >=0.5:
                                _GroupSet['maxF'][j].append(_GroupSet['data4fft'][j]['x'][idx])
                                break
                        except Exception as e:
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            #print(exc_type, fname, exc_tb.tb_lineno)
                            print('Find Max Freq. Error.')
                            _GroupSet['maxF'][j].append(0.0)
                            break
                    #============================================================================
                    _GroupSet['data4main'][j]['x'].append(_pr_x)
                    _GroupSet['data4main'][j]['y'].append(_pr_y)
                    _GroupSet['data4twmp'][j]['x'].append(_tw_x /100)
                    _GroupSet['data4twmp'][j]['y'].append(_tw_y /100)
                    #====================================
                    _chksum = True
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)

                    _GroupSet['data4wave'][j]['y'] = [0] * 512
                    _GroupSet['data4wave'][j]['x'] = list(range(0, len(_GroupSet['data4wave'][j]['y'])))
                    _GroupSet['data4fft'][j]['x'] = [j / (512 *0.008) for j in range(0, 256)]
                    _GroupSet['data4fft'][j]['y'] = [0] *len(_GroupSet['data4fft'][j]['x'])
                    _GroupSet['data4main'][j]['x'].append(65535.0)
                    _GroupSet['data4main'][j]['y'].append(65535.0)
                    _GroupSet['data4twmp'][j]['x'].append(65535.0)
                    _GroupSet['data4twmp'][j]['y'].append(65535.0)

                    _maxAar = sorted(_GroupSet['data4wave'][j]['y'], reverse = True)
                    _GroupSet['maxA'][j].append(_maxAar[0])
            else:   #未觸發
                _GroupSet['data4wave'][j]['y'] = [0] * 512
                _GroupSet['data4wave'][j]['x'] = list(range(0, len(_GroupSet['data4wave'][j]['y'])))
                _GroupSet['data4fft'][j]['x'] = [j / (512 *0.008) for j in range(0, 256)]
                _GroupSet['data4fft'][j]['y'] = [0] *len(_GroupSet['data4fft'][j]['x'])
                _GroupSet['data4main'][j]['x'].append(65535.0)
                _GroupSet['data4main'][j]['y'].append(65535.0)
                _GroupSet['data4twmp'][j]['x'].append(65535.0)
                _GroupSet['data4twmp'][j]['y'].append(65535.0)

                _maxAar = sorted(_GroupSet['data4wave'][j]['y'], reverse = True)
                _GroupSet['maxA'][j].append(_maxAar[0])

            #====================================
            if _chksum: #有觸發且資料新增正確
                try:
                    self._wave  = self._wave  +_GroupSet['data4wave'][j]['y']
                    self._fft  = self._fft  +_GroupSet['data4fft'][j]['y']
                    self._prpd = self._prpd +[_GroupSet['data4main'][j]['x'][-1]] +[_GroupSet['data4main'][j]['y'][-1]]
                    self._twmap = self._twmap +[_GroupSet['data4twmp'][j]['x'][-1]] +[_GroupSet['data4twmp'][j]['y'][-1]]
                    _doublechk['check']  =  _doublechk['check'] +int(_t)    #[0, 1, 2 (=> double check array)]
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                    self._wave = self._wave + ([0] * 512)
                    self._fft = self._fft + ([0] *256)
                    self._prpd = self._prpd + ([65535.0] *2)
                    self._twmap = self._twmap + ([65535.0] *2)
                    _chksum = False

            if _chksum: #有觸發且資料新增正確
                GroupSet[self.gr]['column'][j][Col_i ] = GroupSet[self.gr]['column'][j][Col_i ] +1
                GroupSet[self.gr]['lasttime'][j] = self.triglist[0]
                GroupSet[self.gr]['chxdurat'][j] = round((GroupSet[self.gr]['lasttime'][j] -GroupSet[self.gr]['inittime'][j]), 2)
                GroupSet[self.gr]['chxpds'][j] = GroupSet[self.gr]['chxpds'][j] +1

                #================ 趨勢圖 ==============================================
                if ((self.lasttimepoint not in list(GroupSet[self.gr]['trend']['mv'][j].keys())) or
                    (type(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]) != collections.deque)):
                    GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint] = deque(maxlen = 10)
                    GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint].append(_GroupSet['maxA'][j][0])

                if len(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]) >=10:   #當陣列已填滿
                    idx = [_i for _i in range(0, len(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]))
                           if GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_i] <_GroupSet['maxA'][j][0]]
                    if len(idx) >0: #取代比_maxA小的值
                        #find the min value index for idx
                        _ii = [_i for _i in idx if GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_i] == min(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint])][0]
                        GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_ii] = _GroupSet['maxA'][j][0]
                        pass
                    else:   #陣列的值皆大於 _maxA
                        pass
                else:
                    GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint].append(_GroupSet['maxA'][j][0])

                if self.lasttimepoint not in list(GroupSet[self.gr]['trend']['counters'][j].keys()):
                    GroupSet[self.gr]['trend']['counters'][j][self.lasttimepoint] = 1
                else:
                    GroupSet[self.gr]['trend']['counters'][j][self.lasttimepoint] = GroupSet[self.gr]['trend']['counters'][j][self.lasttimepoint] +1
                #===================================================================

            GroupSet[self.gr]['data4wave'][j]['x'] = _GroupSet['data4wave'][j]['x']
            GroupSet[self.gr]['data4wave'][j]['y'] = _GroupSet['data4wave'][j]['y']
            GroupSet[self.gr]['data4fft'][j]['x'] = _GroupSet['data4fft'][j]['x']
            GroupSet[self.gr]['data4fft'][j]['y'] = _GroupSet['data4fft'][j]['y']
            GroupSet[self.gr]['data4main'][j]['x'].append(_GroupSet['data4main'][j]['x'][0])
            GroupSet[self.gr]['data4main'][j]['y'].append(_GroupSet['data4main'][j]['y'][0])
            GroupSet[self.gr]['data4twmp'][j]['x'].append(_GroupSet['data4twmp'][j]['x'][0])
            GroupSet[self.gr]['data4twmp'][j]['y'].append(_GroupSet['data4twmp'][j]['y'][0])
            self._durat = self._durat +[GroupSet[self.gr]['chxpds'][j], GroupSet[self.gr]['chxdurat'][j],
                                        _GroupSet['maxA'][j][0], GroupSet[self.gr]['lasttime'][j], GroupSet[self.gr]['inittime'][j]]

            #========= 秀數位值 ====================
            if VisualNumPad is not None:
                try:
                    if ((VisualNumPad.ObjID == 'InfoScreen') and (VisualNumPad.gr == self.gr)):
                        vars(VisualNumPad)['maxA%s' %j].set('%.2f'%_GroupSet['maxA'][j][0])
                        vars(VisualNumPad)['maxF%s' %j].set('%.2f' %_GroupSet['maxF'][j][0])
                except:
                    pass
            else:
                pass
        #==========================================================================================================
        if ((_doublechk['check' ]== len(GroupSet[self.gr]['ch'])) and (_doublechk['trigtime'] != None)):   #確認『雙通道』都觸發且資料正確新增
            GroupSet[self.gr]['column'][len(GroupSet[self.gr]['ch'])][_doublechk['trigtime'] ] = GroupSet[self.gr]['column'][len(GroupSet[self.gr]['ch'])][_doublechk['trigtime'] ] +1
            GroupSet[self.gr]['chxpds'][len(GroupSet[self.gr]['ch'])] = _ds
            GroupSet[self.gr]['chxdurat'][len(GroupSet[self.gr]['ch'])] = _dt
            GroupSet[self.gr]['lasttime'][len(GroupSet[self.gr]['ch'])] = _dl
            _maxA = max([self._durat[ii] for ii in (2, 7)])
        else:
            _maxA = 0.0

        _pdstatus = array('d', GroupSet[self.gr]['mmap']['durat'][:])[-1]
        self._durat = self._durat +[
            GroupSet[self.gr]['chxpds'][len(GroupSet[self.gr]['ch'])],
            GroupSet[self.gr]['chxdurat'][len(GroupSet[self.gr]['ch'])], _maxA,
            GroupSet[self.gr]['lasttime'][len(GroupSet[self.gr]['ch'])],
            GroupSet[self.gr]['inittime'][len(GroupSet[self.gr]['ch'])], _pdstatus
            ]   #補上雙通道觸發值

        if _doublechk['check' ] >0: #任一通道有觸發
            for key in GroupSet[self.gr]['mmap'].keys():  #out put mmap file
                #key = 'durat', 'prpd', 'twmap', 'wave', 'fft'
                
                if key == 'durat':
                    float_array = array('d', vars(self)['_%s' %key])
                    pass
                else:
                    float_array = array('f', vars(self)['_%s' %key])
                    pass
                
                if key in ['durat', 'wave', 'fft']:

                    try:
                        GroupSet[self.gr]['mmap'][key].seek(0)
                        float_array.tofile(GroupSet[self.gr]['mmap'][key])
                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        #_ta = [type(item) for item in range(0, len(vars(self)['_%s' %key]))]
                        print(exc_type, fname, exc_tb.tb_lineno,
                              #'mmap:', GroupSet[self.gr]['mmap'][key], 'time:', time.time(),
                              'float_array:', float_array,
                              'key:', key, '%sd' %len(vars(self)['_%s' %key]),
                              #len(vars(self)['_%s' %key]), _ta,
                              GroupSet[self.gr]['mmap'][key].size())
                        #del _ta

                else:

                    if type(GroupSet[self.gr]['mmap'][key]) == mmap.mmap:
                        try:
                            GroupSet[self.gr]['mmap'][key].seek(0, 2)
                            GroupSet[self.gr]['mmap'][key].resize(GroupSet[self.gr]['mmap'][key].size() +(len(float_array) *4))

                            float_array.tofile(GroupSet[self.gr]['mmap'][key])
                        except:
                            print('MMAP Error self.gr:', self.gr, 'key:', key)
                    else:
                        f =open((curPath +('//%s_g%s.~' %(key, self.gr))), 'wb+')
                        float_array.tofile(f)
                        f.close()
                        f =open((curPath +('//%s_g%s.~' %(key, self.gr))), 'ab+')
                        GroupSet[self.gr]['mmap'][key] = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE)
                        UpdateGlobals('GroupSet', GroupSet)
                        print('NEW MMap self.gr:', self.gr, 'key:', key)
                pass

            if isMount:
                #======== output data ============
                #============================
                #pddfile = open((curPath +'//' +linkfile +('_g%s' %self.gr) +".pdd"), "ab+")
                
                try:
                    _pdd = GroupSet[self.gr]['pdd'][:10]
                    if (array('h', _pdd) == array('h', [255] *5)):
                        GroupSet[self.gr]['pdd'].seek(0)
                    else:
                        if GroupSet[self.gr]['pdd'].size() > 3170*9:
                            _tmp = GroupSet[self.gr]['pdd'][3170:]
                            GroupSet[self.gr]['pdd'][:len(_tmp)] = _tmp
                            GroupSet[self.gr]['pdd'].seek(-3170, 2)
                        else:
                            GroupSet[self.gr]['pdd'].resize(GroupSet[self.gr]['pdd'].size() +3170)
                    
                    pddfile = open((outpath +'//' +linkfile +('_g%s' %self.gr) +".pdd"), "ab+")
                    float_array = array('d', [self.triglist[0]])                           #trigtime,len = 1 *8
                    float_array.tofile(pddfile)                                             #trigtime,len = 1 *8
                    float_array.tofile(GroupSet[self.gr]['pdd'])
                    pddfile.write(self.triglist[1])    #command line,len = 1 *9
                    GroupSet[self.gr]['pdd'].write(self.triglist[1])    #command line,len = 1 *9

                    #========= write coef & intercept ==============
                    float_array = array('f', self.calib)    #len = 4 *4
                    float_array.tofile(pddfile)             #len = 4 *4
                    float_array.tofile(GroupSet[self.gr]['pdd'])

                    pddfile.write(self.triglist[2])    #直接寫入 binary data   len = 3127
                    pddfile.write(CFGSessname.zfill(10).encode('ascii'))     #len = 10
                    GroupSet[self.gr]['pdd'].write(self.triglist[2])    #直接寫入 binary data   len = 3127
                    GroupSet[self.gr]['pdd'].write(CFGSessname.zfill(10).encode('ascii'))     #len = 10
                    
                    _splitfile = False
                    #if os.fstat(pddfile.fileno()).st_size >= 1924912760:
                    if os.fstat(pddfile.fileno()).st_size >= 1000000000:
                        _splitfile = True
                    pddfile.close()
                    #======================================================
                    #==================== 分割檔案 ===========================
                    #============== 檔案大小 1GB ================
                    
                    if _splitfile:
                        _lst = glob.glob((outpath +'//' +linkfile +('_g%s.part*' %self.gr)))

                        if len(_lst) >0:
                            _lst2 = [int(item[-3:]) for item in _lst]
                            _part = "{:03d}".format((max(_lst2) +1))
                        else:
                            _part = '000'

                        os.rename((outpath +'//' +linkfile +('_g%s' %self.gr) +".pdd"), (outpath +'//' +linkfile +('_g%s' %self.gr) +(".part%s" %_part)))
                        print('Rename %s to %s' %((outpath +'//' +linkfile +('_g%s' %self.gr) +".pdd"), (outpath +'//' +linkfile +('_g%s' %self.gr) +(".part%s" %_part))))
                except Exception as e:
                    #exc_type, exc_obj, exc_tb = sys.exc_info()
                    #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    #print(exc_type, fname, exc_tb.tb_lineno)
                    pass
                #======================================================
            #==========================================================
        self.in_bin = None
        self.triglist = []
        #print('trigtime:', self.trigtime, 'Gr:', self.gr)
#=============================================
#=============== Get Serial DATA ===================
'''
class TransADConv (threading.Thread):
    def __init__(self, threadID, name, event, stopper):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.event = event
        self.stopper = stopper
        self.in_bin = None

    def run(self):
        global root,GroupSet,Opt2ActFrm,FileCount
        global AlarmCfg,coef,intercept,curPath,BlandFrm

        root.isSuccessful = None
        BlandFrm = GetGlobals('BlandFrm')

        #lKey = {
            #'zh-TW' : lambda : [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if '警 報  設 定' in x][0])][0],
            #'en-US' : lambda : [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if 'AlarmFrm2' in x][0])][0],
            #}.get(AlarmCfg['lang'], lambda : [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if '警 報  設 定' in x][0])][0])()

        for i in GroupSet:
            if AlarmCfg['demo'] != 99:
                BlandFrm.waitproc.set('Group %s' %i +' Opening......')
                GroupSet[i]['ser'] = serial.Serial()
                GroupSet[i]['ser'].port = GroupSet[i]['port']
                #root.waitproc.set('%s Opening......' %GroupSet[i]['ser'].name)
                GroupSet[i]['ser'].baudrate = GroupSet[i]['baudrate']
                GroupSet[i]['ser'].parity = GroupSet[i]['parity']
                GroupSet[i]['ser'].stopbits = GroupSet[i]['stopbits']
                GroupSet[i]['ser'].bytesize  = GroupSet[i]['bytesize']
                GroupSet[i]['ser'].timeout = GroupSet[i]['timeout']
                while not GroupSet[i]['ser'].is_open:
                    GroupSet[i]['ser'].open()
                #print(GroupSet[i]['ser'], 'Open successfully.', 'cmdLine:', GroupSet[i]['cmdline'])
                
            else:
                #root.waitproc.set('Group %s' %i +' Opening......')
                BlandFrm.waitproc.set('Group %s' %i +' Opening......')
                if 'pddsample' not in vars(self) or 'nbyte' not in vars(self):
                    self.pddsample = {}
                    self.nbyte = 3170
        
                try:
                    _f = open((curPath +'//sample' +('_g%s' %i)), "rb")
                    #self.pddsample[i] = _f
                    self.pddsample.update({i : _f})
                    #print(self.pddsample[i].name, 'Open successfully.')
                    
                except:
                    #print('Group %s' %i + ' open file error!')
                    #root.waitproc.set('Group %s' %i + ' open file error!')
                    BlandFrm.waitproc.set('Group %s' %i +' open file error!')
                #time.sleep(1.0)
                
        while self.stopper:# and not self.event.wait(GroupSet[i]['timeout']):
            root.isSuccessful = 1
            
            for i in GroupSet:
                self.trigtime = time.time()
                if AlarmCfg['demo'] != 99:
                    GroupSet[i]['ser'].reset_input_buffer()
                    GroupSet[i]['ser'].reset_output_buffer()
                    #print(len(GroupSet[i]['cmdline']))
                    GroupSet[i]['ser'].write(GroupSet[i]['cmdline'])
                    #self.in_bin = GroupSet[i]['ser'].read(3127)
                    self.in_bin = GroupSet[i]['ser'].readall()
                else:
                    ns = random.randint(0, int(os.stat(self.pddsample[i].name).st_size /self.nbyte)) *self.nbyte
                    self.pddsample[i].seek(ns)
                    self.in_bin = self.pddsample[i].read(self.nbyte)

                global VisualNumPad,subClass,subclass4all
                VisualNumPad = GetGlobals('VisualNumPad')   #<class 'subclass4all.TrigLst'>

                if VisualNumPad is not None:
                    try:
                        if VisualNumPad.ObjID == 'TrigLst':
                            self.log = ('%s || len:%s\n'
                                        %(datetime.datetime.fromtimestamp(self.trigtime).strftime('%Y/%m/%d %H:%M:%S'), len(self.in_bin)))
                            VisualNumPad.triglist.config(state = tk.NORMAL)
                            VisualNumPad.triglist.insert("end", self.log)
                            VisualNumPad.triglist.see('end')
                            VisualNumPad.triglist.config(state = tk.DISABLED)
                            VisualNumPad.triglist.update()
                    except:
                        #print(self.log)
                        pass

                else:
                    #print(self.log)
                    pass

                dlen_chk = {99 : lambda : (len(self.in_bin) >=self.nbyte)}.get(AlarmCfg['demo'], lambda : (len(self.in_bin) >=3127))()

                #if len(self.in_bin) >=3127:
                if dlen_chk:
                    if AlarmCfg['demo'] == 99:
                        self.in_bin = self.in_bin[33:3160]
                        time.sleep(random.uniform(0.0, 1.0))
                    self.splitpdd = splitpdd(i, [self.trigtime, GroupSet[i]['cmdline'], self.in_bin[:3127]])
                    self.splitpdd.run()

                else:
                    if AlarmCfg['demo'] != 99:
                        GroupSet[i]['ser'].reset_input_buffer()
                        GroupSet[i]['ser'].reset_output_buffer()
                    else:
                        time.sleep(random.uniform(0.0, 1.0))
                    
                if not self.stopper:
                    break

            if not self.stopper:
                break

        for i in GroupSet:
            if AlarmCfg['demo'] != 99:
                BlandFrm.waitproc.set(GroupSet[i]['port'] +' Closeding......')
                #root.waitproc.set(GroupSet[i]['port'] +' Closeding......')
                GroupSet[i]['ser'].reset_input_buffer()
                GroupSet[i]['ser'].reset_output_buffer()

                while GroupSet[i]['ser'].is_open:
                    GroupSet[i]['ser'].close()
                    
                #print(GroupSet[i]['port'], 'Closed successfully.')
                #root.waitproc.set(GroupSet[i]['port'] +'Closed successfully.')

            else:
                BlandFrm.waitproc.set('Group %s' %i +' Closeding......')
                #root.waitproc.set('Group %s' %i +' Closeding......')
                self.pddsample[i].close()
                    
                #print(self.pddsample[i].name, 'Closed successfully.')
                #root.waitproc.set('Group %s' %i +'Closed successfully.')
                time.sleep(1.0)

        root.isSuccessful = 0
        del self.in_bin
'''
#=================================================================
'''
class splitpdd():
    def __init__(self, gr, triglist):
        global GroupSet,AlarmCfg,gainDict,curPath,linkfile,CFGSessname,VisualNumPad
        global  trig_chAry,gainDict,gainCali

        self.triglist = triglist
        
        self.gr = gr
        self.gainary = [('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][:4],
                        ('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][-4:]]
        
        trig_chAry = GetGlobals('trig_chAry')
        GroupSet = GetGlobals('GroupSet')
        gainDict = GetGlobals('gainDict')
        gainCali = GetGlobals('gainCali')
    def run(self):
        
        self.lasttimepoint = int((math.ceil(time.time()/(AlarmCfg['TimeInv'] *60))) *AlarmCfg['TimeInv'] *60)      #最新時間點
        #CreatTrend(self.gr, self.lasttimepoint)
        
        self.cmdline = self.triglist[1]
        self.wave_bin = self.triglist[2][:1026]
        self.fft_bin = self.triglist[2][1026:3078]
        self.prpd_bin = self.triglist[2][3078:3098]
        self.twmp_bin = self.triglist[2][3098:3117]
        self.fft_bin = [getSignInt(int.from_bytes(self.fft_bin[_i :(_i +4)], byteorder = 'big')) /100.0 for _i in range(4, len(self.fft_bin), 4)]

        self.calib = []
        for key in GroupSet[self.gr]['mmap'].keys():
            vars(self)['_%s' %key] = [] #產生self._durat, self._prpd, self._twmap, self._wave, self._fft

        _doublechk = {'check' : 0 ,'trigtime' : None}
        Col_i = None
        _t = False
        #_ColAry = [65535.0 for _ci in range(0, len(GroupSet[self.gr]['ch']))]
        #_pr_xAry = [65535.0 for _ci in range(0, len(GroupSet[self.gr]['ch']))]
        #_pr_yAry = [65535.0 for _ci in range(0, len(GroupSet[self.gr]['ch']))]
        for j in range(0, len(GroupSet[self.gr]['ch'])):

            try:
                _g = [_key for _key in gainDict if gainDict[_key][j] == self.gainary[j]][0]
            except Exception as e:
                #exc_type, exc_obj, exc_tb = sys.exc_info()
                #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                #print(exc_type, fname, exc_tb.tb_lineno)
                _g = '10x'

            _ig = int(_g[:2])
            _g = _g.strip()

            coef = GroupSet[self.gr]['Calib'][j]['coef'][_g]
            self.calib.append(coef)
            intercept = GroupSet[self.gr]['Calib'][j]['intercept'][_g]
            self.calib.append(intercept)

            #_pr_y = ((getSignInt(int.from_bytes(self.prpd_bin[(8 +(j *8)) :(12 +(j *8))], byteorder = 'big')) +intercept) * coef)
            _pr_y = getSignInt(int.from_bytes(self.prpd_bin[(8 +(j *8)) :(12 +(j *8))], byteorder = 'big'))
            _pr_x = getSignInt(int.from_bytes(self.prpd_bin[(4 +(j *8)) :(8 +(j *8))], byteorder = 'big'))
            #print(j, _pr_x, _pr_y)
            #if ((_pr_x != 65535.0) and (abs(_pr_y) <= ((1200.0 +intercept) * coef))):
            #if _pr_x != 65535.0 and _pr_y != 65535.0:

            if _pr_x >=0.0 and _pr_x < 360.0:
                #_pr_x = (_pr_x %360.0)  #修復phase值
                _pr_y = (_pr_y +intercept) *coef
                if (AlarmCfg['demo'] ==95):
                    if (trig_chAry[j] != GroupSet[self.gr]['trig_ch']):  #DEMO箱用且非觸發通道
                        _t = ((random.randint(1, 3) %3) ==0)
                    else:
                        pass
                elif (AlarmCfg['demo'] ==99):
                    _chx = int(GroupSet[self.gr]['ch'][j])
                    _t = int((random.randint(1, _chx) %2) ==0)
                    #_t0 = int((random.randint(1, len(GroupSet)) %len(GroupSet)) ==0)
                    #_t0 = int((random.randint(1, 2) %2) ==0)
                    ''''''
                    _t0 = 1
                        
                    if trig_chAry[j] != GroupSet[self.gr]['trig_ch']:
                        _t1 = int((random.randint(1, 3) %3) ==0)
                    else:
                        _t1 = 1
                    _t = bool(_t0 *_t1)
                    ''''''
                    #_t = True
                else:
                    _t = True
            else:
                _t = False	#未觸發

            if _t:
                _pr_y = _pr_y /_ig

                Col_i = math.ceil(_pr_x / AlarmCfg['Col_Range']) *AlarmCfg['Col_Range'] #取觸發通道的相位角
                
                if (trig_chAry[j] == GroupSet[self.gr]['trig_ch']):
                    _doublechk['trigtime'] = Col_i
                    _dl = self.triglist[0]
                    _dt = (GroupSet[self.gr]['lasttime'][len(GroupSet[self.gr]['ch'])]
                           -GroupSet[self.gr]['inittime'][len(GroupSet[self.gr]['ch'])])
                    _dt = round(_dt, 2)
                    _ds = GroupSet[self.gr]['chxpds'][len(GroupSet[self.gr]['ch'])] +1
                
                if GroupSet[self.gr]['isfilter']:
                    #============ highpass ===================
                    #sfb, sfa = signal.butter(4, [0.90, 0.95], 'bandpass')
                    #sfb, sfa = signal.butter(1, [0.52, 0.60], 'bandpass')
                    #sfb, sfa = signal.butter(1, 0.24, 'lowpass')
                    sfb, sfa = signal.butter(4, 0.9, 'highpass')
                    
                    _preFA = [((float(self.wave_bin[i]) +intercept) * coef) /_ig for i in range(2 +(j*512), 514 +(j*512))]
                    GroupSet[self.gr]['data4wave'][j]['y'] = signal.filtfilt(sfb, sfa, _preFA)
                    #=======================================
                else:
                    GroupSet[self.gr]['data4wave'][j]['y'] = [((float(self.wave_bin[i]) +intercept) * coef) /_ig for i in range(2 +(j*512), 514 +(j*512))]

                GroupSet[self.gr]['data4wave'][j]['x'] = list(range(0, len(GroupSet[self.gr]['data4wave'][j]['y'])))

                GroupSet[self.gr]['data4fft'][j]['y'] = self.fft_bin[j *int(len(self.fft_bin)/2) : (j +1) *int(len(self.fft_bin)/2)]
                GroupSet[self.gr]['data4fft'][j]['x'] = [_j / (512 *0.008) for _j in range(0, 256)]

                _tw_x = getSignInt(int.from_bytes(self.twmp_bin[(3 +(j *8)) :(7 +(j *8))], byteorder = 'big'))
                _tw_y = getSignInt(int.from_bytes(self.twmp_bin[(7 +(j *8)) :(11 +(j *8))], byteorder = 'big'))

                #==== 求最大振福與頻率 ============================================================
                #_maxA = max(GroupSet[self.gr]['data4wave'][j]['y'])
                _maxAar = sorted(GroupSet[self.gr]['data4wave'][j]['y'], reverse = True)
                _maxA = sum(_maxAar[0:3])/3
                _fy = sorted(GroupSet[self.gr]['data4fft'][j]['y'], reverse = True)
                idx = 0
                while idx == 0:
                    idx = [_idx for _idx in range(0, len(GroupSet[self.gr]['data4fft'][j]['y'])) if GroupSet[self.gr]['data4fft'][j]['y'][_idx] == _fy[0]][0]
                    _fy.pop(0)
                    if GroupSet[self.gr]['data4fft'][j]['x'][idx] >=0.5:
                        break

                _maxF = GroupSet[self.gr]['data4fft'][j]['x'][idx]
                #============================================================================

                GroupSet[self.gr]['column'][j][Col_i ] = GroupSet[self.gr]['column'][j][Col_i ] +1
                GroupSet[self.gr]['data4main'][j]['x'].append(_pr_x)
                GroupSet[self.gr]['data4main'][j]['y'].append(_pr_y)
                GroupSet[self.gr]['data4twmp'][j]['x'].append(_tw_x /100)
                GroupSet[self.gr]['data4twmp'][j]['y'].append(_tw_y /100)

                GroupSet[self.gr]['lasttime'][j] = self.triglist[0]
                GroupSet[self.gr]['chxdurat'][j] = round((GroupSet[self.gr]['lasttime'][j] -GroupSet[self.gr]['inittime'][j]), 2)
                #GroupSet[self.gr]['chxpds'][j] = len(GroupSet[self.gr]['data4main'][j]['y'])
                GroupSet[self.gr]['chxpds'][j] = GroupSet[self.gr]['chxpds'][j] +1

                #========= 秀數位值 ====================
                if VisualNumPad is not None:
                    try:
                        if ((VisualNumPad.ObjID == 'InfoScreen') and (VisualNumPad.gr == self.gr)):
                            vars(VisualNumPad)['maxA%s' %j].set('%.2f'%_maxA)
                            vars(VisualNumPad)['maxF%s' %j].set('%.2f' %_maxF)
                    except:
                        pass
                else:
                    pass
                #====================================
                #================ 趨勢圖 ==============================================
                if ((self.lasttimepoint not in list(GroupSet[self.gr]['trend']['mv'][j].keys())) or
                    (type(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]) != collections.deque)):
                    #_v = GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]
                    GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint] = deque(maxlen = 10)
                    GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint].append(_maxA)

                if len(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]) >=10:   #當陣列已填滿
                    #find the index for less than _maxA
                    idx = [_i for _i in range(0, len(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]))
                           if GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_i] <_maxA]
                    if len(idx) >0: #取代比_maxA小的值
                        #find the min value index for idx
                        _ii = [_i for _i in idx if GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_i] == min(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint])][0]
                        #replace the index of _ii
                        GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_ii] = _maxA
                        pass
                    else:   #陣列的值皆大於 _maxA
                        pass
                else:
                    GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint].append(_maxA)

                if self.lasttimepoint not in list(GroupSet[self.gr]['trend']['counters'][j].keys()):
                    GroupSet[self.gr]['trend']['counters'][j][self.lasttimepoint] = 1
                else:
                    GroupSet[self.gr]['trend']['counters'][j][self.lasttimepoint] = GroupSet[self.gr]['trend']['counters'][j][self.lasttimepoint] +1
                #===================================================================
                    
                _doublechk['check']  =  _doublechk['check'] +int(_t)    #[0, 1, 2 (=> double check array)]
            else:
                _maxAar = sorted(GroupSet[self.gr]['data4wave'][j]['y'], reverse = True)
                _maxA = sum(_maxAar[0:3])/3
                GroupSet[self.gr]['data4wave'][j]['y'] = [0] * 512
                GroupSet[self.gr]['data4wave'][j]['x'] = list(range(0, len(GroupSet[self.gr]['data4wave'][j]['y'])))
                GroupSet[self.gr]['data4fft'][j]['x'] = [j / (512 *0.008) for j in range(0, 256)]
                GroupSet[self.gr]['data4fft'][j]['y'] = [0] *len(GroupSet[self.gr]['data4fft'][j]['x'])
                GroupSet[self.gr]['data4main'][j]['x'].append(65535.0)
                GroupSet[self.gr]['data4main'][j]['y'].append(65535.0)
                GroupSet[self.gr]['data4twmp'][j]['x'].append(65535.0)
                GroupSet[self.gr]['data4twmp'][j]['y'].append(65535.0)

            self._wave  = self._wave  +GroupSet[self.gr]['data4wave'][j]['y']
            self._fft  = self._fft  +GroupSet[self.gr]['data4fft'][j]['y']
            self._prpd = self._prpd +[GroupSet[self.gr]['data4main'][j]['x'][-1]] +[GroupSet[self.gr]['data4main'][j]['y'][-1]]
            self._twmap = self._twmap +[GroupSet[self.gr]['data4twmp'][j]['x'][-1]] +[GroupSet[self.gr]['data4twmp'][j]['y'][-1]]
            #self._durat = self._durat +[GroupSet[self.gr]['chxpds'][j], GroupSet[self.gr]['chxdurat'][j], GroupSet[self.gr]['lasttime'][j]]
            #print(_maxA)
            self._durat = self._durat +[GroupSet[self.gr]['chxpds'][j], GroupSet[self.gr]['chxdurat'][j], _maxA,
                                        GroupSet[self.gr]['lasttime'][j], GroupSet[self.gr]['inittime'][j]]

        if ((_doublechk['check' ]== len(GroupSet[self.gr]['ch'])) and (_doublechk['trigtime'] != None)):   #確認『雙通道』都觸發且資料正確新增
            GroupSet[self.gr]['column'][len(GroupSet[self.gr]['ch'])][_doublechk['trigtime'] ] = GroupSet[self.gr]['column'][len(GroupSet[self.gr]['ch'])][_doublechk['trigtime'] ] +1
            GroupSet[self.gr]['chxpds'][len(GroupSet[self.gr]['ch'])] = _ds
            GroupSet[self.gr]['chxdurat'][len(GroupSet[self.gr]['ch'])] = _dt
            GroupSet[self.gr]['lasttime'][len(GroupSet[self.gr]['ch'])] = _dl
            _maxA = max([self._durat[ii] for ii in (2, 7)])

        self._durat = self._durat +[
            GroupSet[self.gr]['chxpds'][len(GroupSet[self.gr]['ch'])],
            GroupSet[self.gr]['chxdurat'][len(GroupSet[self.gr]['ch'])], _maxA,
            GroupSet[self.gr]['lasttime'][len(GroupSet[self.gr]['ch'])],
            GroupSet[self.gr]['inittime'][len(GroupSet[self.gr]['ch'])]
            ]

        if _doublechk['check' ] >0: #任一通道有觸發
            for key in GroupSet[self.gr]['mmap'].keys():  #out put mmap file
                #key = 'durat', 'prpd', 'twmap', 'wave', 'fft'
                if key == 'durat':
                    pass
                else:
                    float_array = array('f', vars(self)['_%s' %key])
                
                if key in ['durat', 'wave', 'fft']:
                    GroupSet[self.gr]['mmap'][key].seek(0)
                    if key == 'durat':
                        try:
                            GroupSet[self.gr]['mmap'][key].write(struct.pack('%sd' %len(vars(self)['_%s' %key]), *vars(self)['_%s' %key]))
                        except Exception as e:
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            print(exc_type, fname, exc_tb.tb_lineno)
                        pass
                    else:
                        float_array.tofile(GroupSet[self.gr]['mmap'][key])

                else:

                    if type(GroupSet[self.gr]['mmap'][key]) == mmap.mmap:
                        GroupSet[self.gr]['mmap'][key].seek(0, 2)
                        GroupSet[self.gr]['mmap'][key].resize(GroupSet[self.gr]['mmap'][key].size() +(len(float_array) *4))
                        float_array.tofile(GroupSet[self.gr]['mmap'][key])
                    else:
                        f =open((curPath +('//%s_g%s.~' %(key, self.gr))), 'wb+')
                        float_array.tofile(f)
                        f.close()
                        f =open((curPath +('//%s_g%s.~' %(key, self.gr))), 'ab+')
                        GroupSet[self.gr]['mmap'][key] = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE)
                        UpdateGlobals('GroupSet', GroupSet)
                pass

            #======== output data ============
            #============================
            pddfile = open((curPath +'//' +linkfile +('_g%s' %self.gr) +".pdd"),"ab+")
            float_array = array('d', [self.triglist[0]])                           #trigtime,len = 1 *8
            float_array.tofile(pddfile)
            pddfile.write(self.triglist[1])    #command line,len = 1 *9

            #========= write coef & intercept ==============
            float_array = array('f', self.calib)    #len = 4 *4
            float_array.tofile(pddfile)

            pddfile.write(self.triglist[2])    #直接寫入 binary data   len = 3127
            pddfile.write(CFGSessname.zfill(10).encode('ascii'))     #len = 10
            pddfile.close()
            #======================================================
        #lKey = [key for key in list(Opt2ActFrm.keys()) if  Opt2ActFrm[key][1] == 'MainFrm2'][0]
        #Opt2ActFrm[lKey][2].updatechart()
'''
#=======================================================================
#=======================================================================
#====================== def OutputTrend(gr, lasttimepoint) =========================
def OutputTrend():
    global GroupSet,AlarmCfg

    lasttimepoint = int((math.ceil(time.time()/(AlarmCfg['TimeInv'] *60))) *AlarmCfg['TimeInv'] *60)      #最新時間點
    for i in GroupSet:      #Create mv_gr?.trend, counters_gr?.trend ......
        for key in GroupSet[i]['trend']:
            _meanV = [lasttimepoint]
            for j in range(0, len(GroupSet[i]['ch'])):
                if lasttimepoint in list(GroupSet[i]['trend'][key][j].keys()):
                    _meanV.append(np.mean(GroupSet[i]['trend'][key][j][lasttimepoint]))
                else:
                    _meanV.append(0.0)
                '''
                try:
                    _meanV.append(np.mean(GroupSet[i]['trend'][key][j][lasttimepoint]))
                except:
                    _meanV.append(0.0)
                '''
            _t = struct.pack('Iff', *_meanV)

            _isChk = False
            if type(GroupSet[i]['trend'][key]['fd']) == mmap.mmap:
                _isChk = True
                pass
            else:
                f = open(GroupSet[i]['trend'][key]['fd'], "ab+")
                if ((os.path.isfile(GroupSet[i]['trend'][key]['fd'])) and
                    (os.stat(GroupSet[i]['trend'][key]['fd']).st_size >0)):
                    _isChk = True
                    pass
                else:
                    f.write(_t)
                    f.close()
                    f = open(GroupSet[i]['trend'][key]['fd'], "ab+")
                GroupSet[i]['trend'][key]['fd'] = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE)
                '''
                if not os.path.isfile(GroupSet[i]['trend'][key]['fd']):
                    f = open(GroupSet[i]['trend'][key]['fd'], "ab+")
                    f.close()
                    
                if os.stat(GroupSet[i]['trend'][key]['fd']).st_size >0:
                    f = open(GroupSet[i]['trend'][key]['fd'], 'ab+')
                    GroupSet[i]['trend'][key]['fd'] = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE)
                    _isChk = True
                else:
                    f = open(GroupSet[i]['trend'][key]['fd'], "ab+")
                    f.write(_t)
                    f.close()
                    f = open(GroupSet[i]['trend'][key]['fd'], 'ab+')
                    GroupSet[i]['trend'][key]['fd'] = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE)
                '''

            if _isChk:
                nrec = int(GroupSet[i]['trend'][key]['fd'].size() /12)
                _tmp = struct.unpack('Iff' *nrec, GroupSet[i]['trend'][key]['fd'])
                _idx = [item for item in range(0, len(_tmp), 3) if _tmp[item] == lasttimepoint]
                if len(_idx) >0:    #已有值，即更新
                    _idx = _idx[0]
                    GroupSet[i]['trend'][key]['fd'].seek(int((_idx /3) *12), 0)
                    #GroupSet[i]['trend'][key]['fd'].seek(4, 1)
                else:
                    GroupSet[i]['trend'][key]['fd'].seek(0, 2)
                    GroupSet[i]['trend'][key]['fd'].resize(GroupSet[i]['trend'][key]['fd'].size() +len(_t))
                GroupSet[i]['trend'][key]['fd'].write(_t)
            UpdateGlobals('GroupSet', GroupSet)
                        
#===========================================================
#====================== def CreatTrend(gr) =========================
'''
def CreatTrend(gr, lasttimepoint):
    global GroupSet

    for j in range(0, len(GroupSet[gr]['ch'])):
        #=================== Create Trend Spline =====================
        #print(j, lasttimepoint, GroupSet[gr]['trend']['mv'][j].keys())
        if (lasttimepoint) not in GroupSet[gr]['trend']['mv'][j].keys():     #當產生有新的一筆，求前10大放電量平均，並寫入
            GroupSet[gr]['trend']['mv'][j][lasttimepoint] = deque(maxlen = 10)
            if len(list(GroupSet[gr]['trend']['mv'][j].keys())) >=2: #已有歷史值
                _key = list(GroupSet[gr]['trend']['mv'][j].keys())[-2]
                if type(GroupSet[gr]['trend']['mv'][j][_key]) == collections.deque:  #現正處理的值
                    if len(GroupSet[gr]['trend']['mv'][j][_key]) >0:
                        _meanV = np.mean(GroupSet[gr]['trend']['mv'][j][_key])
                    else:
                        _meanV = 0.0
                else:   #從 *.trend 撈回的值
                    _meanV = GroupSet[gr]['trend']['mv'][j][_key]

                GroupSet[gr]['trend']['mv'][j][_key] = _meanV

                if j == 0:
                    _t = struct.pack('If', lasttimepoint, GroupSet[gr]['trend']['mv'][j][_key])
                    pass
                else:
                    _t = struct.pack('f', GroupSet[gr]['trend']['mv'][j][_key])
                    pass

                if type(GroupSet[gr]['trend']['mv']['fd']) == mmap.mmap:
                    GroupSet[gr]['trend']['mv']['fd'].seek(0, 2)
                    GroupSet[gr]['trend']['mv']['fd'].resize(GroupSet[gr]['trend']['mv']['fd'].size() +len(_t))
                    GroupSet[gr]['trend']['mv']['fd'].write(_t)
                else:
                    _fd = open(GroupSet[gr]['trend']['mv']['fd'], "ab+")
                    _fd.write(_t)
                    _fd.close()
                    _fd = open(GroupSet[gr]['trend']['mv']['fd'], "ab+")
                    GroupSet[gr]['trend']['mv']['fd'] = mmap.mmap(_fd.fileno(), 0, access = mmap.ACCESS_WRITE)
                    UpdateGlobals('GroupSet', GroupSet)

                ''''''
                _fd = open(GroupSet[gr]['trend']['mv']['fd'], "ab+")

                if j == 0:
                    _t = struct.pack('If', lasttimepoint, GroupSet[gr]['trend']['mv'][j][_key])
                    pass
                else:
                    _t = struct.pack('f', GroupSet[gr]['trend']['mv'][j][_key])
                    pass
                #print(_key, GroupSet[gr]['trend']['mv'][j][_key])
                _fd.write(_t)
                _fd.close()
                ''''''
        else:   #表初始啟動
            pass

        if (lasttimepoint) not in GroupSet[gr]['trend']['counters'][j].keys():     #求放電量次數
            GroupSet[gr]['trend']['counters'][j][lasttimepoint] = 0
                    
            if len(list(GroupSet[gr]['trend']['counters'][j].keys())) >=2:
                _key = list(GroupSet[gr]['trend']['counters'][j].keys())[-2]
                #_fd = open(GroupSet[gr]['trend']['counters']['fd'], "ab+")
                if j == 0:
                    _t = struct.pack('If', lasttimepoint, GroupSet[gr]['trend']['counters'][j][_key])
                    pass
                else:
                    _t = struct.pack('f', GroupSet[gr]['trend']['counters'][j][_key])
                    pass

                #_fd.write(_t)
                #_fd.close()

                if type(GroupSet[gr]['trend']['counters']['fd']) == mmap.mmap:
                    GroupSet[gr]['trend']['counters']['fd'].seek(0, 2)
                    GroupSet[gr]['trend']['counters']['fd'].resize(GroupSet[gr]['trend']['counters']['fd'].size() +len(_t))
                    GroupSet[gr]['trend']['counters']['fd'].write(_t)
                else:
                    _fd = open(GroupSet[gr]['trend']['counters']['fd'], "ab+")
                    _fd.write(_t)
                    _fd.close()
                    _fd = open(GroupSet[gr]['trend']['counters']['fd'], "ab+")
                    GroupSet[gr]['trend']['counters']['fd'] = mmap.mmap(_fd.fileno(), 0, access = mmap.ACCESS_WRITE)
                    UpdateGlobals('GroupSet', GroupSet)
                pass
            else:   #表初始啟動
                pass
'''
#======================================================
'''
class splitpdd2():
    def __init__(self, gr, triglist):
        global GroupSet,AlarmCfg,gainDict,curPath,linkfile,CFGSessname,curPath
        #global FFilter_variable
        self.triglist = triglist
        #print(self.triglist[0], self.triglist[1])
        self.gr = gr
        self.gainary = [('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][:4],
                        ('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][-4:]]
        gainDict = GetGlobals('gainDict')
        gainCali = GetGlobals('gainCali')
    
    def run(self):
        
        self.lasttimepoint = int((math.ceil(time.time()/(AlarmCfg['TimeInv'] *60))) *AlarmCfg['TimeInv'] *60)      #最新時間點
        CreatTrend(self.gr, self.lasttimepoint)
        
        self.cmdline = self.triglist[1]
        self.wave_bin = self.triglist[2][:1026]
        self.fft_bin = self.triglist[2][1026:3078]
        self.prpd_bin = self.triglist[2][3078:3098]
        self.twmp_bin = self.triglist[2][3098:3117]
        self.fft_bin = [getSignInt(int.from_bytes(self.fft_bin[_i :(_i +4)], byteorder = 'big')) /100.0 for _i in range(4, len(self.fft_bin), 4)]
        
        self.calib = []
        for key in GroupSet[self.gr]['mmap'].keys():
            vars(self)['_%s' %key] = []

        _doublechk = {'check' : 0 ,'trigtime' : None}
        _t = False
        for j in range(0, len(GroupSet[self.gr]['ch'])):

            try:
                _g = [_key for _key in gainDict if gainDict[_key][j] == self.gainary[j]][0]
            except Exception as e:
                #exc_type, exc_obj, exc_tb = sys.exc_info()
                #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                #print(exc_type, fname, exc_tb.tb_lineno)
                _g = '10x'

            _ig = int(_g[:2])
            _g = _g.strip()

            coef = GroupSet[self.gr]['Calib'][j]['coef'][_g]
            self.calib.append(coef)
            intercept = GroupSet[self.gr]['Calib'][j]['intercept'][_g]
            self.calib.append(intercept)

            ''''''
            _isSim = False
            #=========== 模擬降躁 =========
            if j == 0 and GroupSet[self.gr]['isfilter']:
                _isSim = True

            #============================================
            ''''''
                    
            _pr_y = ((getSignInt(int.from_bytes(self.prpd_bin[(8 +(j *8)) :(12 +(j *8))], byteorder = 'big')) +intercept) * coef)
            _pr_x = getSignInt(int.from_bytes(self.prpd_bin[(4 +(j *8)) :(8 +(j *8))], byteorder = 'big'))
            _pr_x = (_pr_x %360.0)  #修復phase值
            
            if (AlarmCfg['demo'] /10) ==9:  #DEMO箱用
                if trig_chAry[j] != GroupSet[self.gr]['trig_ch']:   #非觸發通道
                    _t = ((random.randint(1,10) %3) ==0)
                else:
                    _t = True
            else:   #廠測
                _t = True

            if _t:

                Col_i = math.ceil(_pr_x / AlarmCfg['Col_Range']) *AlarmCfg['Col_Range']
                _pr_y = _pr_y /_ig
                
                #if _isSim:
                if GroupSet[self.gr]['isfilter']:
                    #sfb, sfa = signal.butter(4, [0.90, 0.95], 'bandpass')
                    #sfb, sfa = signal.butter(1, [0.52, 0.60], 'bandpass')
                    #sfb, sfa = signal.butter(1, 0.24, 'lowpass')
                    sfb, sfa = signal.butter(4, 0.9, 'highpass')
                    
                    _preFA = [((float(self.wave_bin[i]) +intercept) * coef) /_ig for i in range(2 +(j*512), 514 +(j*512))]
                    GroupSet[self.gr]['data4wave'][j]['y'] = signal.filtfilt(sfb, sfa, _preFA)
                    
                else:
                    GroupSet[self.gr]['data4wave'][j]['y'] = [((float(self.wave_bin[i]) +intercept) * coef) /_ig for i in range(2 +(j*512), 514 +(j*512))]
                GroupSet[self.gr]['data4fft'][j]['y'] = self.fft_bin[j *int(len(self.fft_bin)/2) : (j +1) *int(len(self.fft_bin)/2)]
                _tw_y = getSignInt(int.from_bytes(self.twmp_bin[(7 +(j *8)) :(11 +(j *8))], byteorder = 'big'))

                GroupSet[self.gr]['data4wave'][j]['x'] = list(range(0, len(GroupSet[self.gr]['data4wave'][j]['y'])))
                GroupSet[self.gr]['data4fft'][j]['x'] = [j / (512 *0.008) for j in range(0, 256)]
                _tw_x = getSignInt(int.from_bytes(self.twmp_bin[(3 +(j *8)) :(7 +(j *8))], byteorder = 'big'))


                #==== 求最大振福與頻率 ============================================================
                #_maxA = max(GroupSet[self.gr]['data4wave'][j]['y'])
                _maxAar = sorted(GroupSet[self.gr]['data4wave'][j]['y'], reverse = True)
                _maxA = sum(_maxAar[0:3])/3
                _fy = sorted(GroupSet[self.gr]['data4fft'][j]['y'], reverse = True)
                idx = 0
                while idx == 0:
                    idx = [_idx for _idx in range(0, len(GroupSet[self.gr]['data4fft'][j]['y'])) if GroupSet[self.gr]['data4fft'][j]['y'][_idx] == _fy[0]][0]
                    _fy.pop(0)
                    if GroupSet[self.gr]['data4fft'][j]['x'][idx] >=0.5:
                        break

                _maxF = GroupSet[self.gr]['data4fft'][j]['x'][idx]
                #============================================================================

                GroupSet[self.gr]['column'][j][Col_i ] = GroupSet[self.gr]['column'][j][Col_i ] +1
                GroupSet[self.gr]['data4main'][j]['x'].append(_pr_x)
                GroupSet[self.gr]['data4main'][j]['y'].append(_pr_y)
                GroupSet[self.gr]['data4twmp'][j]['x'].append(_tw_x /100)
                GroupSet[self.gr]['data4twmp'][j]['y'].append(_tw_y /100)

                GroupSet[self.gr]['lasttime'][j] = self.triglist[0]
                GroupSet[self.gr]['chxdurat'][j] = (GroupSet[self.gr]['lasttime'][j] -GroupSet[self.gr]['inittime'][j])
                GroupSet[self.gr]['chxpds'][j] = len(GroupSet[self.gr]['data4main'][j]['y'])

                #========= 秀數位值 ====================
                if VisualNumPad is not None:
                    try:
                        if ((VisualNumPad.ObjID == 'InfoScreen') and (VisualNumPad.gr == self.gr)):
                            vars(VisualNumPad)['maxA%s' %j].set('%.2f'%_maxA)
                            vars(VisualNumPad)['maxF%s' %j].set('%.2f' %_maxF)
                    except:
                        pass
                else:
                    pass
                #====================================
                #================ 趨勢圖 ==============================================
                if type(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]) != collections.deque:
                    _v = GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]
                    GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint] = deque(maxlen = 10)
                    GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint].append(_v)

                if len(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]) >=10:
                    idx = [_i for _i in range(0, len(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint])) if GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_i] <_maxA]
                    if len(idx) >0:
                        _ii = [_i for _i in idx if GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_i] == min(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint])][0]
                        GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_ii] = _maxA
                        pass
                    else:
                        GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint].append(_maxA)
                GroupSet[self.gr]['trend']['counters'][j][self.lasttimepoint] = GroupSet[self.gr]['trend']['counters'][j][self.lasttimepoint] +1
                #===================================================================
                if _doublechk['trigtime']:
                    _doublechk['trigtime'] = Col_i #雙通道Column值取觸發通道者
                    
                _doublechk['check']  =  _doublechk['check'] +int(_t)    #[0, 1, 2 (=> double check array)]
            else:
                GroupSet[self.gr]['data4wave'][j]['y'] = [0] * 512
                GroupSet[self.gr]['data4wave'][j]['x'] = list(range(0, len(GroupSet[self.gr]['data4wave'][j]['y'])))
                GroupSet[self.gr]['data4fft'][j]['x'] = [j / (512 *0.008) for j in range(0, 256)]
                GroupSet[self.gr]['data4fft'][j]['y'] = [0] *len(GroupSet[self.gr]['data4fft'][j]['x'])
                GroupSet[self.gr]['data4main'][j]['x'].append(65535.0)
                GroupSet[self.gr]['data4main'][j]['y'].append(65535.0)
                GroupSet[self.gr]['data4twmp'][j]['x'].append(65535.0)
                GroupSet[self.gr]['data4twmp'][j]['y'].append(65535.0)

        if _doublechk['check' ]== len(GroupSet[self.gr]['ch']):   #確認『雙通道』都觸發且資料正確新增
            GroupSet[self.gr]['column'][len(GroupSet[self.gr]['ch'])][Col_i ] = GroupSet[self.gr]['column'][len(GroupSet[self.gr]['ch'])][Col_i ] +1

        if _doublechk['check' ] >0: #任一通道有觸發
            for key in GroupSet[self.gr]['mmap'].keys():  #out put mmap file
                #key = 'durat', 'prpd', 'twmap', 'wave', 'fft'
                GroupSet[self.gr]['mmap'][key] =open((curPath +('//%s_g%s.~' %(key, self.gr))), 'rb+')
                if key in ['durat', 'wave', 'fft']:
                    GroupSet[self.gr]['mmap'][key].seek(0)

                float_array = array('f', vars(self)['_%s' %key])
                float_array.tofile(GroupSet[self.gr]['mmap'][key])
                GroupSet[self.gr]['mmap'][key].close()
                pass

            #======== output data ============
            #============================
            pddfile = open((curPath +'//' +linkfile +('_g%s' %self.gr) +".pdd"),"ab+")
            float_array = array('d', [self.triglist[0]])                           #trigtime,len = 1 *8
            float_array.tofile(pddfile)
            pddfile.write(self.triglist[1])    #command line,len = 1 *9

            #========= write coef & intercept ==============
            float_array = array('f', self.calib)    #len = 4 *4
            float_array.tofile(pddfile)

            pddfile.write(self.triglist[2])    #直接寫入 binary data   len = 3127
            pddfile.write(CFGSessname.zfill(10).encode('ascii'))     #len = 10
            pddfile.close()

            #======================================================
'''
#==============================================================
'''
class splitpdd99():
    def __init__(self, gr, triglist):
        global GroupSet,AlarmCfg,gainDict,curPath,linkfile,CFGSessname,VisualNumPad
        global  gainDict,gainCali
        self.triglist = triglist
        #print(self.triglist[0], self.triglist[1])
        self.gr = gr
        self.gainary = [('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][:4],
                        ('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][-4:]]
        gainDict = GetGlobals('gainDict')
        gainCali = GetGlobals('gainCali')
    def run(self):
        
        self.lasttimepoint = int((math.ceil(time.time()/(AlarmCfg['TimeInv'] *60))) *AlarmCfg['TimeInv'] *60)      #最新時間點
        CreatTrend(self.gr, self.lasttimepoint)
        #self.CreatTrend()
        
        self.cmdline = self.triglist[1]
        self.wave_bin = self.triglist[2][:1026]
        self.fft_bin = self.triglist[2][1026:3078]
        self.prpd_bin = self.triglist[2][3078:3098]
        self.twmp_bin = self.triglist[2][3098:3117]

        self.fft_bin = [getSignInt(int.from_bytes(self.fft_bin[_i :(_i +4)], byteorder = 'big')) /100.0 for _i in range(4, len(self.fft_bin), 4)]

        self.calib = []
        for key in GroupSet[self.gr]['mmap'].keys():
            vars(self)['_%s' %key] = []

        _doublechk = {'check' : 0 ,'trigtime' : None}
        for j in range(0, len(GroupSet[self.gr]['ch'])):

            try:
                _g = [_key for _key in gainDict if gainDict[_key][j] == self.gainary[j]][0]
            except Exception as e:
                #exc_type, exc_obj, exc_tb = sys.exc_info()
                #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                #print(exc_type, fname, exc_tb.tb_lineno)
                _g = '10x'

            _ig = int(_g[:2])
            _g = _g.strip()

            coef = GroupSet[self.gr]['Calib'][j]['coef'][_g]
            self.calib.append(coef)
            intercept = GroupSet[self.gr]['Calib'][j]['intercept'][_g]
            self.calib.append(intercept)

            _pr_y = ((getSignInt(int.from_bytes(self.prpd_bin[(8 +(j *8)) :(12 +(j *8))], byteorder = 'big')) +intercept) * coef)
            _pr_x = getSignInt(int.from_bytes(self.prpd_bin[(4 +(j *8)) :(8 +(j *8))], byteorder = 'big'))
            _pr_x = (_pr_x %360.0)  #修復phase值

            _doublechk = {'check' : 0 ,'trigtime' : None}
            _t = False
            if _pr_x < 360.0:
                _t = True
                _doublechk['trigtime'] = True
            else:
                _t = False

            if _t:
                _datachk = False
                #_pr_x = getSignInt(int.from_bytes(self.prpd_bin[(4 +(j *8)) :(8 +(j *8))], byteorder = 'big'))
                Col_i = math.ceil(_pr_x / AlarmCfg['Col_Range']) *AlarmCfg['Col_Range']
                if Col_i in list(GroupSet[self.gr]['column'][j].keys()):  #確認角度資料是否正確
                    _datachk = True

            if (_t and _datachk):   #有觸發且資料正確                        if (_t and _datachk):   #有觸發且資料正確
                ''''''
                try:
                    _g = [key for key in gainDict if gainDict[key][j] == self.gainary[j]][0]
                except:
                    _g = '10x'

                _g = int(_g[:2])
                ''''''
                _pr_y = _maxA = _pr_y /_ig

                GroupSet[self.gr]['data4wave'][j]['y'] = [((float(self.wave_bin[i]) +intercept) * coef) /_ig for i in range(2 +(j*512), 514 +(j*512))]
                GroupSet[self.gr]['data4wave'][j]['x'] = list(range(0, len(GroupSet[self.gr]['data4wave'][j]['y'])))

                GroupSet[self.gr]['data4fft'][j]['y'] = self.fft_bin[j *int(len(self.fft_bin)/2) : (j +1) *int(len(self.fft_bin)/2)]
                GroupSet[self.gr]['data4fft'][j]['x'] = [j / (512 *0.008) for j in range(0, 256)]

                _tw_x = getSignInt(int.from_bytes(self.twmp_bin[(3 +(j *8)) :(7 +(j *8))], byteorder = 'big'))
                _tw_y = getSignInt(int.from_bytes(self.twmp_bin[(7 +(j *8)) :(11 +(j *8))], byteorder = 'big'))

                GroupSet[self.gr]['column'][j][Col_i ] = GroupSet[self.gr]['column'][j][Col_i ] +1
                GroupSet[self.gr]['data4main'][j]['x'].append(_pr_x)
                GroupSet[self.gr]['data4main'][j]['y'].append(_pr_y)
                GroupSet[self.gr]['data4twmp'][j]['x'].append(_tw_x /100)
                GroupSet[self.gr]['data4twmp'][j]['y'].append(_tw_y /100)
                #print(j, _pr_x, _pr_y)
                GroupSet[self.gr]['lasttime'][j] = self.triglist[0]
                GroupSet[self.gr]['chxdurat'][j] = (GroupSet[self.gr]['lasttime'][j] -GroupSet[self.gr]['inittime'][j])
                GroupSet[self.gr]['chxpds'][j] = len(GroupSet[self.gr]['data4main'][j]['y'])

                if VisualNumPad is not None:
                    try:
                        if ((VisualNumPad.ObjID == 'InfoScreen') and (VisualNumPad.gr == self.gr)):
                            vars(VisualNumPad)['maxA%s' %j].set(_maxA)
                            idx = [idx for idx in range(0, len(GroupSet[self.gr]['data4fft'][j]['y'])) if GroupSet[self.gr]['data4fft'][j]['y'][idx] == max(GroupSet[self.gr]['data4fft'][j]['y'])][0]
                            _maxF = GroupSet[self.gr]['data4fft'][j]['x'][idx]
                            vars(VisualNumPad)['maxF%s' %j].set(_maxF)

                    except:
                        pass

                else:
                    pass

                #================ 趨勢圖 ==============================================
                if type(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]) != collections.deque:
                    _v = GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]
                    GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint] = deque(maxlen = 10)
                    GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint].append(_v)

                if len(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint]) >=10:
                    idx = [_i for _i in range(0, len(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint])) if GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_i] <_maxA]
                    if len(idx) >0:
                        _ii = [_i for _i in idx if GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_i] == min(GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint])][0]
                        GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint][_ii] = _maxA
                        pass
                    else:
                        GroupSet[self.gr]['trend']['mv'][j][self.lasttimepoint].append(_maxA)
                GroupSet[self.gr]['trend']['counters'][j][self.lasttimepoint] = GroupSet[self.gr]['trend']['counters'][j][self.lasttimepoint] +1
                #===================================================================
                if _doublechk['trigtime']:
                    _doublechk['trigtime'] = Col_i #雙通道Column值取觸發通道者
                    
                _doublechk['check']  =  _doublechk['check'] +int(_t)    #[0, 1, 2 (=> double check array)]
            else:
                _pr_x = _pr_y = 65535.0
                GroupSet[self.gr]['data4wave'][j]['y'] = [0] * 512
                GroupSet[self.gr]['data4wave'][j]['x'] = list(range(0, len(GroupSet[self.gr]['data4wave'][j]['y'])))
                GroupSet[self.gr]['data4fft'][j]['x'] = [j / (512 *0.008) for j in range(0, 256)]
                GroupSet[self.gr]['data4fft'][j]['y'] = [0] *len(GroupSet[self.gr]['data4fft'][j]['x'])
                GroupSet[self.gr]['data4main'][j]['x'].append(65535.0)
                GroupSet[self.gr]['data4main'][j]['y'].append(65535.0)
                GroupSet[self.gr]['data4twmp'][j]['x'].append(65535.0)
                GroupSet[self.gr]['data4twmp'][j]['y'].append(65535.0)

            self._wave  = self._wave  +GroupSet[self.gr]['data4wave'][j]['y']
            self._fft  = self._fft  +GroupSet[self.gr]['data4fft'][j]['y']
            self._prpd = self._prpd +[GroupSet[self.gr]['data4main'][j]['x'][-1]] +[GroupSet[self.gr]['data4main'][j]['y'][-1]]
            self._twmap = self._twmap +[GroupSet[self.gr]['data4twmp'][j]['x'][-1]] +[GroupSet[self.gr]['data4twmp'][j]['y'][-1]]
            self._durat = self._durat +[GroupSet[self.gr]['chxpds'][j], GroupSet[self.gr]['chxdurat'][j], GroupSet[self.gr]['lasttime'][j]]

            GroupSet[self.gr]['mmap']['prpd'] =open((curPath +('//prpd_g%s.~' %self.gr)), 'ab+')
            GroupSet[self.gr]['mmap']['prpd'].write(struct.pack('ff', _pr_x,_pr_y))
            GroupSet[self.gr]['mmap']['prpd'].close()

        if _doublechk['check' ]== len(GroupSet[self.gr]['ch']):   #確認『雙通道』都觸發且資料正確新增
            GroupSet[self.gr]['column'][len(GroupSet[self.gr]['ch'])][Col_i ] = GroupSet[self.gr]['column'][len(GroupSet[self.gr]['ch'])][Col_i ] +1

        if _doublechk['check' ] >0: #任一通道有觸發
            for key in GroupSet[self.gr]['mmap'].keys():  #out put mmap file
                #key = 'durat', 'prpd', 'twmap', 'wave', 'fft'
                #GroupSet[self.gr]['mmap'][key] =open((curPath +('//%s_g%s.~' %(key, self.gr))), 'ab+')
                if key in ['durat', 'wave', 'fft']:
                    GroupSet[self.gr]['mmap'][key] =open((curPath +('//%s_g%s.~' %(key, self.gr))), 'rb+')
                    GroupSet[self.gr]['mmap'][key].seek(0)

                    float_array = array('f', vars(self)['_%s' %key])
                    float_array.tofile(GroupSet[self.gr]['mmap'][key])
                    GroupSet[self.gr]['mmap'][key].close()
                pass

            #======== output data ============
            #============================
            pddfile = open((curPath +'//' +linkfile +('_g%s' %self.gr) +".pdd"),"ab+")
            float_array = array('d', [self.triglist[0]])                           #trigtime,len = 1 *8
            float_array.tofile(pddfile)
            pddfile.write(self.triglist[1])    #command line,len = 1 *9

            #========= write coef & intercept ==============
            float_array = array('f', self.calib)    #len = 4 *4
            float_array.tofile(pddfile)

            pddfile.write(self.triglist[2])    #直接寫入 binary data   len = 3127
            pddfile.write(CFGSessname.zfill(10).encode('ascii'))     #len = 10
            pddfile.close()

    ''''''
    def CreatTrend(self):
        global GroupSet

        for i in [self.gr]:
            for j in range(0, len(GroupSet[i]['ch'])):
                #=================== Create Trend Spline =====================
                if (self.lasttimepoint) not in GroupSet[i]['trend']['mv'][j].keys():     #求前10大放電量平均
                    GroupSet[i]['trend']['mv'][j][self.lasttimepoint] = deque(maxlen = 10)
                    if len(list(GroupSet[i]['trend']['mv'][j].keys())) >=2: #已有歷史值

                        _key = list(GroupSet[i]['trend']['mv'][j].keys())[-2]
                        if type(GroupSet[i]['trend']['mv'][j][_key]) == collections.deque:  #現正處理的值
                            if len(GroupSet[i]['trend']['mv'][j][_key]) >0:
                                _meanV = np.mean(GroupSet[i]['trend']['mv'][j][_key])
                            else:
                                _meanV = 0.0
                        else:   #從 *.trend 撈回的值
                            _meanV = GroupSet[i]['trend']['mv'][j][_key]

                        GroupSet[i]['trend']['mv'][j][_key] = _meanV

                        _fd = open(GroupSet[i]['trend']['mv']['fd'], "ab+")
                        
                        if j == 0:
                            _t = struct.pack('If', self.lasttimepoint, GroupSet[i]['trend']['mv'][j][_key])
                            pass
                        else:
                            _t = struct.pack('f', GroupSet[i]['trend']['mv'][j][_key])
                            pass
                        _fd.write(_t)
                        _fd.close()
                else:   #表初始啟動
                    pass

                if (self.lasttimepoint) not in GroupSet[i]['trend']['counters'][j].keys():     #求放電量次數
                    GroupSet[i]['trend']['counters'][j][self.lasttimepoint] = 0
                    
                    if len(list(GroupSet[i]['trend']['counters'][j].keys())) >=2:
                        _key = list(GroupSet[i]['trend']['counters'][j].keys())[-2]
                        _fd = open(GroupSet[i]['trend']['counters']['fd'], "ab+")
                        if j == 0:
                            _t = struct.pack('If', self.lasttimepoint, GroupSet[i]['trend']['counters'][j][_key])
                            pass
                        else:
                            _t = struct.pack('f', GroupSet[i]['trend']['counters'][j][_key])
                            pass

                        _fd.write(_t)
                        _fd.close()
                        pass
                    else:   #表初始啟動
                        pass
    '''
                #======================================================
#=============== class thread4GetColumn(threading.Thread) ===========
'''
class GetColumn(threading.Thread):  #更新放電資料
    def __init__(self, threadID, name, event, stopper):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.event = event
        self.stopper = stopper
        self.fd = {}
        
    def run(self):
        global GroupSet,AlarmCfg,curPath,linkfile,CFGSessname,gainDict,viewGP

        while self.stopper and not self.event.wait(AlarmCfg['period']):

            self.lasttimepoint = int((math.ceil(time.time()/(AlarmCfg['TimeInv'] *60))) *AlarmCfg['TimeInv'] *60)      #最新時間點

            self.CreatTrend()
            for i in GroupSet:

                try:
                    vars(self)['_lastrecord_g%s' %i]
                except:
                    vars(self)['_lastrecord_g%s' %i] = None

                self.gainary = [('00000000' +bin(GroupSet[i]['gain'])[2:])[-8:][:4],
                                ('00000000' +bin(GroupSet[i]['gain'])[2:])[-8:][-4:]]
                    
                while ((len(GroupSet[i]['triglist']) >0) and (GroupSet[i]['triglist'][0][0] != vars(self)['_lastrecord_g%s' %i])):#(GroupSet[i]['triglist'][0] != vars(self)['_lastrecord_g%s' %i])):

                    _t0 = time.time()
                    #注意：多群組以正在顯示(viewGP)為優先
                    #======= 分離特徵 ==============
                    self.cmdline = GroupSet[i]['triglist'][0][1]
                    self.wave_bin = GroupSet[i]['triglist'][0][2][:1026]
                    self.fft_bin = GroupSet[i]['triglist'][0][2][1026:3078]
                    self.prpd_bin = GroupSet[i]['triglist'][0][2][3078:3098]
                    self.twmp_bin = GroupSet[i]['triglist'][0][2][3098:3117]

                    self.fft_bin = [getSignInt(int.from_bytes(self.fft_bin[_i :(_i +4)], byteorder = 'big')) /100.0 for _i in range(4, len(self.fft_bin), 4)]

                    self.calib = []
                    for key in GroupSet[i]['mmap'].keys():
                        vars(self)['_%s' %key] = []

                    _doublechk = {'check' : 0 ,'trigtime' : None}
                    for j in range(0, len(GroupSet[i]['ch'])):

                        coef = GroupSet[i]['Calib'][j]['coef']
                        self.calib.append(coef)
                        intercept = GroupSet[i]['Calib'][j]['intercept']
                        self.calib.append(intercept)

                        _pr_y = ((getSignInt(int.from_bytes(self.prpd_bin[(8 +(j *8)) :(12 +(j *8))], byteorder = 'big')) +intercept) * coef)
                        _t = _datachk = False

                        if abs(_pr_y) >= GroupSet[i]['trig_lv']:
                            _t = True
                            _doublechk['trigtime'] = True
                        else:
                            _t = False

                        if _t:
                            _datachk = False
                            _pr_x = getSignInt(int.from_bytes(self.prpd_bin[(4 +(j *8)) :(8 +(j *8))], byteorder = 'big'))
                            Col_i = math.ceil(_pr_x / AlarmCfg['Col_Range']) *AlarmCfg['Col_Range']
                            if Col_i in list(GroupSet[i]['column'][j].keys()):  #確認角度資料是否正確
                                _datachk = True

                        if (_t and _datachk):   #有觸發且資料正確
                        
                            try:
                                _g = [key for key in gainDict if gainDict[key][j] == self.gainary[j]][1]
                            except:
                                _g = '10x'
                                
                            _g = int(_g[:2])
                            GroupSet[i]['data4wave'][j]['y'] = [((float(self.wave_bin[i]) +intercept) * coef) /_g for i in range(2 +(j*512), 514 +(j*512))]
                            GroupSet[i]['data4wave'][j]['x'] = list(range(0, len(GroupSet[i]['data4wave'][j]['y'])))

                            GroupSet[i]['data4fft'][j]['y'] = self.fft_bin[j *int(len(self.fft_bin)/2) : (j +1) *int(len(self.fft_bin)/2)]
                            GroupSet[i]['data4fft'][j]['x'] = [j / (512 *0.008) for j in range(0, 256)]

                            _pr_y = _maxA = _pr_y /_g
                            
                            _tw_x = getSignInt(int.from_bytes(self.twmp_bin[(3 +(j *8)) :(7 +(j *8))], byteorder = 'big'))
                            _tw_y = getSignInt(int.from_bytes(self.twmp_bin[(7 +(j *8)) :(11 +(j *8))], byteorder = 'big'))
                            
                            GroupSet[i]['column'][j][Col_i ] = GroupSet[i]['column'][j][Col_i ] +1

                            GroupSet[i]['data4main'][j]['x'].append(_pr_x)
                            GroupSet[i]['data4main'][j]['y'].append(_pr_y)

                            GroupSet[i]['data4twmp'][j]['x'].append(_tw_x /100)
                            GroupSet[i]['data4twmp'][j]['y'].append(_tw_y /100)

                            GroupSet[i]['lasttime'][j] = GroupSet[i]['triglist'][0][0]
                            GroupSet[i]['chxdurat'][j] = (GroupSet[i]['lasttime'][j] -GroupSet[i]['inittime'][j])
                            GroupSet[i]['chxpds'][j] = len(GroupSet[i]['data4main'][j]['y'])

                            #================ 趨勢圖 ==============================================
                            if type(GroupSet[i]['trend']['mv'][j][self.lasttimepoint]) != collections.deque:
                                _v = GroupSet[i]['trend']['mv'][j][self.lasttimepoint]
                                GroupSet[i]['trend']['mv'][j][self.lasttimepoint] = deque(maxlen = 10)
                                GroupSet[i]['trend']['mv'][j][self.lasttimepoint].append(_v)
                                
                            if len(GroupSet[i]['trend']['mv'][j][self.lasttimepoint]) >=10:
                                idx = [_i for _i in range(0, len(GroupSet[i]['trend']['mv'][j][self.lasttimepoint])) if GroupSet[i]['trend']['mv'][j][self.lasttimepoint][_i] <_maxA]
                                if len(idx) >0:
                                    _ii = [_i for _i in idx if GroupSet[i]['trend']['mv'][j][self.lasttimepoint][_i] == min(GroupSet[i]['trend']['mv'][j][self.lasttimepoint])][0]
                                    GroupSet[i]['trend']['mv'][j][self.lasttimepoint][_ii] = _maxA
                                    pass
                            else:
                                GroupSet[i]['trend']['mv'][j][self.lasttimepoint].append(_maxA)
                            GroupSet[i]['trend']['counters'][j][self.lasttimepoint] = GroupSet[i]['trend']['counters'][j][self.lasttimepoint] +1
                            #===================================================================

                            if _doublechk['trigtime']:
                                _doublechk['trigtime'] = Col_i #雙通道Column值取觸發通道者

                            _doublechk['check']  =  _doublechk['check'] +int(_t)    #[0, 1, 2 (=> double check array)]

                        else:
                            GroupSet[i]['data4wave'][j]['y'] = [0] * (len(GroupSet[i]['data4wave'][j]['y']))
                            GroupSet[i]['data4fft'][j]['y'] = [0] *(len(GroupSet[i]['data4fft'][j]['y']))
                            GroupSet[i]['data4main'][j]['x'].append(255)
                            GroupSet[i]['data4main'][j]['y'].append(255)
                            GroupSet[i]['data4twmp'][j]['x'].append(255)
                            GroupSet[i]['data4twmp'][j]['y'].append(255)

                        self._wave  = self._wave  +GroupSet[i]['data4wave'][j]['y']
                        self._fft  = self._fft  +GroupSet[i]['data4fft'][j]['y']
                        self._prpd = self._prpd +[GroupSet[i]['data4main'][j]['x'][-1]] +[GroupSet[i]['data4main'][j]['y'][-1]]
                        self._twmap = self._twmap +[GroupSet[i]['data4twmp'][j]['x'][-1]] +[GroupSet[i]['data4twmp'][j]['y'][-1]]
                        self._durat = self._durat +[GroupSet[i]['chxpds'][j], GroupSet[i]['chxdurat'][j], GroupSet[i]['lasttime'][j]]

                    if _doublechk['check' ]== len(GroupSet[i]['ch']):   #確認『雙通道』都觸發且資料正確新增
                        GroupSet[i]['column'][len(GroupSet[i]['ch'])][Col_i ] = GroupSet[i]['column'][len(GroupSet[i]['ch'])][Col_i ] +1

                    if _doublechk['check' ] >0: #任一通道有觸發
                        for key in GroupSet[i]['mmap'].keys():  #out put mmap file
                            if key in ['prpd', 'twmap']:
                                GroupSet[i]['mmap'][key] =open((curPath +('//%s_g%s.~' %(key, i))), 'ab+')
                            else:
                                GroupSet[i]['mmap'][key] =open((curPath +('//%s_g%s.~' %(key, i))), 'wb')

                            float_array = array('f', vars(self)['_%s' %key])
                            float_array.tofile(GroupSet[i]['mmap'][key])
                            GroupSet[i]['mmap'][key].close()
                            pass

                        #======== output data ============
                        #============================
                        pddfile = open((curPath +'//' +linkfile +('_g%s' %i) +".pdd"),"ab+")
                        float_array = array('d', [GroupSet[i]['triglist'][0][0]])                           #trigtime,len = 1 *8
                        float_array.tofile(pddfile)
                        pddfile.write(GroupSet[i]['triglist'][0][1])    #command line,len = 1 *9

                        #========= write coef & intercept ==============
                        float_array = array('f', self.calib)    #len = 4 *4
                        float_array.tofile(pddfile)
                        
                        pddfile.write(GroupSet[i]['triglist'][0][2])    #直接寫入 binary data   len = 3127
                        pddfile.write(CFGSessname.zfill(10).encode('ascii'))     #len = 10
                        pddfile.close()
                    
                    vars(self)['_lastrecord_g%s' %i] = GroupSet[i]['triglist'][0][0]
                    GroupSet[i]['triglist'].pop(0)  #刪除 第 0筆 資料
                    if (time.time() -_t0) >1.0:
                        break
                    pass
                pass

    def CreatTrend(self):
        global GroupSet

        for i in GroupSet:
            for j in range(0, len(GroupSet[i]['ch'])):
                #=================== Create Trend Spline =====================
                if (self.lasttimepoint) not in GroupSet[i]['trend']['mv'][j].keys():     #求前10大放電量平均
                    GroupSet[i]['trend']['mv'][j][self.lasttimepoint] = deque(maxlen = 10)
                    #print(type(GroupSet[i]['trend']['mv'][j][self.lasttimepoint]))
                    if len(list(GroupSet[i]['trend']['mv'][j].keys())) >=2: #已有歷史值

                        _key = list(GroupSet[i]['trend']['mv'][j].keys())[-2]
                        if type(GroupSet[i]['trend']['mv'][j][_key]) == collections.deque:  #現正處理的值
                            if len(GroupSet[i]['trend']['mv'][j][_key]) >0:
                                _meanV = np.mean(GroupSet[i]['trend']['mv'][j][_key])
                            else:
                                _meanV = 0.0
                        else:   #從 *.trend 撈回的值
                            _meanV = GroupSet[i]['trend']['mv'][j][_key]

                        GroupSet[i]['trend']['mv'][j][_key] = _meanV

                        _fd = open(GroupSet[i]['trend']['mv']['fd'], "ab+")
                        
                        if j == 0:
                            _t = struct.pack('If', self.lasttimepoint, GroupSet[i]['trend']['mv'][j][_key])
                            pass
                        else:
                            _t = struct.pack('f', GroupSet[i]['trend']['mv'][j][_key])
                            pass
                        _fd.write(_t)
                        _fd.close()
                else:   #表初始啟動
                    pass

                if (self.lasttimepoint) not in GroupSet[i]['trend']['counters'][j].keys():     #求放電量次數
                    GroupSet[i]['trend']['counters'][j][self.lasttimepoint] = 0
                    
                    if len(list(GroupSet[i]['trend']['counters'][j].keys())) >=2:
                        _key = list(GroupSet[i]['trend']['counters'][j].keys())[-2]
                        _fd = open(GroupSet[i]['trend']['counters']['fd'], "ab+")
                        if j == 0:
                            _t = struct.pack('If', self.lasttimepoint, GroupSet[i]['trend']['counters'][j][_key])
                            pass
                        else:
                            _t = struct.pack('f', GroupSet[i]['trend']['counters'][j][_key])
                            pass

                        _fd.write(_t)
                        _fd.close()
                        pass
                    else:   #表初始啟動
                        pass

                #======================================================
#=================================================================
'''
#================ 演算法執行序 ================================
class CalcuPhase(threading.Thread):
    def __init__(self, threadID, name, col_sel):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.col_sel = col_sel #structure : {i : {wry_gr[j] : []}}
        self.PDStatus = {}
        '''
        self.x_diff_limi0 = 30
        self.x_diff_limi1 = 160
        self.x_diff_limi2 = 220
        self.WeightL_limi0 = 0.8
        self.WeightR_limi0 = 0.8
        self.WeightL_limi1 = 0.6
        self.WeightR_limi1 = 0.6
        '''
        
    def run(self):
        global threadLock,GroupSet,AlarmCfg#,curPath,Col_Range,RealStatus,Alert,ProcessForm
        #global Alert,msgbl4Alert
        #global Config4alarm,reset,Config4col,Config4hist
        # 獲得鎖，成功獲得鎖定後返回True
        # 可選的timeout參數不填時將一直阻塞直到獲得鎖定
        # 否則超時後將返回False

        '''
        threadLock.acquire()
        # 釋放鎖
        if threadLock == "locked":
            threadLock.release()
        '''
        for i in self.col_sel.keys():   # i == _grp
            self.PDStatus[i] = {}
            for j in list(self.col_sel[i].keys()):  # j == ch
                #if int(AlarmCfg['demo'] /10) ==9:
                
                if int(AlarmCfg['demo']) == 95:
                    self.isalert = True
                elif int(AlarmCfg['demo']) == 2:
                    self.isalert, x_diff, WeightL, WeightR, sigma_y0 = self.subModel(i, j, 60, 145, 235, 0.65, 0.65, 0.45, 0.45)
                #elif int(AlarmCfg['demo']) == 98:
                    #self.isalert, x_diff, WeightL, WeightR, sigma_y0 = self.subModel(i, j, 0, 360, 0, 1.0, 1.0, 1.0, 1.0)

                else:
                    self.isalert, x_diff, WeightL, WeightR, sigma_y0 = self.subModel(i, j, 30, 160, 220, 0.8, 0.8, 0.6, 0.6)

                #self.isalert = True
                if self.isalert:
                    '''
                    if j == 2:
                        self.PDStatus.update({i : {j : 2}})
                    else:
                        self.PDStatus.update({i : {j : 1}})
                    '''
                    #self.PDStatus.update({i : {j : 1}})
                    self.PDStatus[i][j] = 1
                    #print(self.PDStatus[i][j])
                else:
                    #self.PDStatus.update({i : {j : 1}})
                    #self.PDStatus.update({i : {j : 0}})
                    self.PDStatus[i][j] = 0

    def subModel(self, i, j, x_diff_limi0, x_diff_limi1, x_diff_limi2, WeightL_limi0, WeightR_limi0, WeightL_limi1, WeightR_limi1):
        global StatusBar
        StatusBar = GetGlobals('StatusBar')
        _gri = StatusBar.showgrouplnk[i][0]
        _n = [_ch for _ch in range(0, len(list(self.col_sel[i].keys()))) if list(self.col_sel[i].keys())[_ch] == j][0]
        BarArray0 = list((GroupSet[_gri]['column'][_n]).items())
        column_array0 = np.array(BarArray0, dtype=[('deg', float), ('count', float)])
        sigma_xy0 = np.sum(column_array0['deg']* column_array0['count'])
        sigma_y0 = np.sum(column_array0['count'])

        try:
            centr0 = math.ceil((sigma_xy0 / sigma_y0) / AlarmCfg['Col_Range']) *AlarmCfg['Col_Range']
            rowL = np.where(column_array0['deg'] < centr0)
            rowR = np.where(column_array0['deg'] >= centr0)
            column_arrayL = np.array(column_array0[rowL], dtype=[('deg', float), ('count', float)])
            column_arrayR = np.array(column_array0[rowR], dtype=[('deg', float), ('count', float)])
            sigma_xyL = np.sum(column_arrayL['deg']* column_arrayL['count'])
            sigma_yL = np.sum(column_arrayL['count'])
            centrL = sigma_xyL / sigma_yL
            sigma_xyR = np.sum(column_arrayR['deg']* column_arrayR['count'])
            sigma_yR = np.sum(column_arrayR['count'])
            centrR = sigma_xyR / sigma_yR
            x_diff = centrR -centrL
            centrL = math.ceil(centrL / AlarmCfg['Col_Range']) *AlarmCfg['Col_Range']
            centrR = math.ceil(centrR / AlarmCfg['Col_Range']) *AlarmCfg['Col_Range']
            rowL = np.where(((column_arrayL['deg'] >= (centrL -(2 *AlarmCfg['Col_Range']))) &
                             (column_arrayL['deg'] <= (centrL +(2 *AlarmCfg['Col_Range'])))))
            rowR = np.where(((column_arrayR['deg'] >= (centrR -(2 *AlarmCfg['Col_Range']))) &
                             (column_arrayR['deg'] <= (centrR +(2 *AlarmCfg['Col_Range'])))))
            Weight_arrayL = np.array(column_arrayL[rowL], dtype=[('deg', float), ('count', float)])
            Weight_arrayR = np.array(column_arrayR[rowR], dtype=[('deg', float), ('count', float)])
            WeightL = np.sum(Weight_arrayL['count']) /np.sum(column_arrayL['count'])
            WeightR = np.sum(Weight_arrayR['count']) /np.sum(column_arrayR['count'])

            if (x_diff < x_diff_limi0 and
                WeightL > WeightL_limi0 and WeightR > WeightR_limi0):
                _isalert = True
                pass
            elif (x_diff > x_diff_limi1 and x_diff < x_diff_limi2 and
                  WeightL > WeightL_limi1 and WeightR > WeightR_limi1):
                _isalert = True
                pass
            else:
                _isalert = False
                pass

            #print(i, j, x_diff, WeightL, WeightR)
        except: #注意，當兩通到個別時間滿足(無雙通道一起觸發)，產生錯誤
            #self.PDStatus.update({i : {j : 1}})
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            self.PDStatus.update({i : {j : 0}})
            _isalert = False
            x_diff = WeightL = WeightR  = sigma_y0
            pass

        return _isalert, x_diff, WeightL, WeightR, sigma_y0

#=======================================================
#================= class getstatus(threading.Thread) ==========================
class getstatus(threading.Thread):
    def __init__(self, threadID, name, event, stopper):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.event = event
        self.stopper = stopper
        self.oldstatus = {}
        self.thread4Calcu = []
        
    def run(self):
        global AlarmCfg,Opt2ActFrm,status
        global threadLock,StatusBar,trivitem,gainDict
        while self.stopper and not self.event.wait(AlarmCfg['period']):
            self.hist = {}
            thisAlertTime = time.localtime()
            rst_gr = []
            alt_gr = {}
            wry_gr = {}
            StatusBar = GetGlobals('StatusBar')
            GroupSet = GetGlobals('GroupSet')
            AlarmCfg = GetGlobals('AlarmCfg')
            status = GetGlobals('status')
            _tempA = {}
            [_tempA.update({ii : array('d', GroupSet[ii]['mmap']['durat'][:])}) for ii in GroupSet]

            for i in _tempA:    #len(_tempA) == len(GroupSet)
                _t0 = time.time()
                _count = [_tempA[i][_idx] for _idx in range(0, len(_tempA[i]) -1, 5)]   #[ch0, ch1, (ch0 +ch1)]
                _durat = [_tempA[i][_idx +1] for _idx in range(0, len(_tempA[i]) -1, 5)]    #[ch0, ch1, (ch0 +ch1)]
                _lastT = [_tempA[i][_idx +3] for _idx in range(0, len(_tempA[i]) -1, 5)]    #[ch0, ch1, (ch0 +ch1)]
                _pdstatus = _tempA[i][-1]

                #========================================================================

                _alt_gr = [j for j in range(0, len(GroupSet[i]['ch']))
                           if ((_count[j] >AlarmCfg['maxpoint']) and (_durat[j] >AlarmCfg['maxdurat']))]    #[0, 1], [0], [1]
                
                if len(_alt_gr) >int(not(AlarmCfg['chx_sel'])): #告警等級 #雙通道時 len(_alt_gr) == 2，單通道時 len(_alt_gr) == 1
                    
                    self.hist.update({i :{ 'cmdline' : GroupSet[i]['cmdline'],
                                           'data4main' : GroupSet[i]['data4main'],
                                           'data4twmp' : GroupSet[i]['data4twmp'],
                                           'chxpds' : _count,#GroupSet[i]['chxpds'],
                                           'chxdurat' : _durat,#GroupSet[i]['chxdurat']
                                           '_tempA' : _tempA
                                           }})

                    #======================================================================
                    _gainary = [('00000000' +bin(GroupSet[i]['gain'])[2:])[-8:][:4],
                                ('00000000' +bin(GroupSet[i]['gain'])[2:])[-8:][-4:]]
                    _chgain = [[_j, _i][1] for _j in range(0, len(GroupSet[i]['ch'])) for _i in range(0, len(list(gainDict.keys()))) if gainDict[list(gainDict.keys())[_i]][_j] == _gainary[_j]]
                    _temp_y = [[abs(GroupSet[i]['data4main'][_j]['y'][item]) for item in range(0, len(GroupSet[i]['data4main'][_j]['y']))
                                       if GroupSet[i]['data4main'][_j]['y'][item] != 65535.0] for _j in range(0, len(GroupSet[i]['ch']))]
                    _temp_y = [sorted(_temp_y[_j]) for _j in range(0, len(GroupSet[i]['ch']))]
                    _temp_y = [_temp_y[_j][2 *int(len(_temp_y[_j]) /3)] *int(list(gainDict.keys())[_chgain[_j]][:2]) for _j in range(0, len(GroupSet[i]['ch']))]
                    _minlv = min(_temp_y)
                    _trigch = _temp_y.index(_minlv)
                    _realev = min([_i for _i in list(trivitem.values()) if _i <= _minlv], key = lambda x : abs(x -_minlv))
                    _setlev = GroupSet[i]['trig_lv']
                    _chglevOld = max([_realev, _setlev])
                    _idx = [_idx for _idx in list(trivitem.keys()) if trivitem[_idx] == _chglevOld][0]
                    del _realev, _setlev
                    #print('_chglevOld:', _chglevOld, '_minlv:', _minlv, '_idx:', _idx)
                    if _chglevOld  < max(list(trivitem.values())):
                        _trigch = GroupSet[i]['trig_ch']
                        _chglev = _chglevOld
                        while _chglev == _chglevOld:
                            _idx = str(int(_idx) +1)        #Triv Lv. ↑
                            _chglev = trivitem[_idx]
                        _chgain = GroupSet[i]['gain']
                        #print('_chglev:', _chglev,'type _chglev:', type(_chglev), '_idx:', _idx, '_chgain:', _chgain)
                        pass
                    else:
                        if all( _val == 0 for _val in _chgain): #can't lower gain
                            _trigch, _chglev, _chgain = GroupSet[i]['trig_ch'], GroupSet[j]['trig_lv'], GroupSet[i]['gain']
                        else:
                            _trigch, _chglev = GroupSet[i]['trig_ch'], GroupSet[j]['trig_lv']   #can't upper TrigLv.
                            _chgain = [(_chgain[i] -int(_chgain[i] >0)) for i in range(0, len(_chgain))]
                            _chgain = int((reduce(lambda x, y: x +y, [gainDict[list(gainDict.keys())[_chgain[x]]][x] for x in range(0, len(_chgain))])), 2)
                        pass
                    GroupSet[i]['autotrig'] = [_trigch, _chglev, _chgain]   #ex.[16, 600.0, 126]

                    #======================================================================
                    #_grpA = self.convGri2Grp(i, _alt_gr)
                    _grpA = convGri2Grp(i, _alt_gr)

                    for _grp in _grpA:  #雙通道時 len(_grpA) == 1，單通道時 len(_grpA) == 1 or 2
                        alt_gr[_grp] = {}
                        [alt_gr[_grp].update({j : []}) for j in _alt_gr]
                        rst_gr.append(_grp)
                        if _grp in list(self.oldstatus.keys()):    #刪除舊狀態
                            self.oldstatus.pop(_grp)
                        pass

                        #print('alert:', StatusBar.showgrouplnk[_grp])
                    pass
                else:   #clear even
                    _rst_gr = [j for j in range(0, len(GroupSet[i]['ch']))
                               if (_t0 -_lastT[j]) >10.0]
                    
                    if len(_rst_gr) >0: #reset 群組，_rst_gr = [0, 1], [0], [1]
                        #print('_rst_gr:', _rst_gr)
                        #======================================================================
                        if bool(status):
                            _gainary = [('00000000' +bin(GroupSet[i]['gain'])[2:])[-8:][:4],
                                        ('00000000' +bin(GroupSet[i]['gain'])[2:])[-8:][-4:]]
                            _chgain = [[_j, _i][1] for _j in range(0, len(GroupSet[i]['ch'])) for _i in range(0, len(list(gainDict.keys()))) if gainDict[list(gainDict.keys())[_i]][_j] == _gainary[_j]]
                            _minlv = max(list(trivitem.values()))
                            _trigch = GroupSet[i]['trig_ch']
                            _idx = (list(trivitem.keys())[list(trivitem.values()).index(GroupSet[i]['trig_lv'])])
                            if int(_idx) > 1:
                                _chglev = trivitem[str(int(_idx) -1)]
                                _chgain = GroupSet[i]['gain']
                                pass
                            else:
                                if all( _val == (len(list(gainDict.keys())) -1) for _val in _chgain): #can't upper gain
                                    #_trigch, _chglev, _chgain = GroupSet[i]['trig_ch'], GroupSet[j]['trig_lv'], GroupSet[i]['gain']
                                    _trigch, _chglev, _chgain = False, False, False
                                else:
                                    _trigch, _chglev = GroupSet[i]['trig_ch'], GroupSet[i]['trig_lv']  #can't lower TrigLv.
                                    _chgain = [(_chgain[i] +int(_chgain[i] <(len(list(gainDict.keys()))) -1)) for i in range(0, len(_chgain))]
                                    _chgain = int((reduce(lambda x, y: x +y, [gainDict[list(gainDict.keys())[_chgain[x]]][x] for x in range(0, len(_chgain))])), 2)
                                pass
                            GroupSet[i]['autotrig'] = [_trigch, _chglev, _chgain]
                        else:   #暫停狀態
                            GroupSet[i]['autotrig'] = [None, None, None]
                        #======================================================================
                        
                        #_grpA = self.convGri2Grp(i, _rst_gr)    #副程式直接轉換Grp，雙通道時 len(_grpA) == 1
                        _grpA = convGri2Grp(i, _rst_gr)    #副程式直接轉換Grp，雙通道時 len(_grpA) == 1
                        for _grp in _grpA:
                            rst_gr.append(_grp)
                            #print('reset:', StatusBar.showgrouplnk[_grp])   #reset: [0, '2通道', [1], [2]]

                        pass
                    else:
                        if len(_alt_gr) == 1: #雙通道觸發，警示等級，單通道時 跳過
                            #_grpA = self.convGri2Grp(i, _alt_gr)    #副程式直接轉換Grp，雙通道時 len(_grpA) == 1
                            _grpA = convGri2Grp(i, _alt_gr)    #副程式直接轉換Grp，雙通道時 len(_grpA) == 1

                            self.hist.update({i :{ 'cmdline' : GroupSet[i]['cmdline'],
                                                   'data4main' : GroupSet[i]['data4main'],
                                                   'data4twmp' : GroupSet[i]['data4twmp'],
                                                   'chxpds' : _count,#GroupSet[i]['chxpds'],
                                                   'chxdurat' : _durat,#GroupSet[i]['chxdurat']
                                                   '_tempA' : _tempA
                                                   }})

                            for _grp in _grpA:
                                if _grp in list(self.oldstatus.keys()): #已有舊狀態
                                    if (((_count[_alt_gr[0]] -self.oldstatus[_grp][_alt_gr[0]][0]) >(AlarmCfg['maxpoint'] /2)) and
                                        ((_durat[_alt_gr[0]] -self.oldstatus[_grp][_alt_gr[0]][1]) >(AlarmCfg['maxdurat'] /2))):     #狀態超過maxpoint /2 且 maxdurat /2

                                        wry_gr.update({_grp : {_alt_gr[0] : []}})    
                                        self.oldstatus[_grp][_alt_gr[0]][0] = _count[_alt_gr[0]]#GroupSet[i]['chxpds'][(_wry_gr[j])]
                                        self.oldstatus[_grp][_alt_gr[0]][1] = _durat[_alt_gr[0]]#GroupSet[i]['chxdurat'][(_wry_gr[j])]
                                    pass
                                else:   #第一次新增
                                    self.oldstatus[_grp] = {}
                                    self.oldstatus[_grp].update({_alt_gr[0] : [_count[_alt_gr[0]], _durat[_alt_gr[0]] ,thisAlertTime]})
                                    wry_gr[_grp] = {}
                                    wry_gr[_grp].update({_alt_gr[0] : []})
                        else:
                            _part = 1/(int(AlarmCfg['chx_sel']) +1) #1 || 1/2，雙通道時 _part = 1，單通道時 _part = 1/2
                            _wry_gr = [j for j in range(0, len(GroupSet[i]['ch']))
                                       if ((_count[j] >AlarmCfg['maxpoint'] *_part) and (_durat[j] >AlarmCfg['maxdurat'] *_part))]
                            if len(_wry_gr) >0: #warry 群組

                                self.hist.update({i :{ 'cmdline' : GroupSet[i]['cmdline'],
                                                       'data4main' : GroupSet[i]['data4main'],
                                                       'data4twmp' : GroupSet[i]['data4twmp'],
                                                       'chxpds' : _count,#GroupSet[i]['chxpds'],
                                                       'chxdurat' : _durat,#GroupSet[i]['chxdurat']
                                                       '_tempA' : _tempA
                                                       }})
                                
                                for j in range(0, len(_wry_gr)):
                                    #_grpA = self.convGri2Grp(i, [_wry_gr[j]]) #副程式直接轉換Grp
                                    _grpA = convGri2Grp(i, [_wry_gr[j]]) #副程式直接轉換Grp
                                    for _grp in _grpA:
                                        if _grp in list(self.oldstatus.keys()): #已有舊狀態
                                            if (((_count[_wry_gr[j]] -self.oldstatus[_grp][_wry_gr[j]][0]) >(AlarmCfg['maxpoint'] *_part/2)) and
                                                ((_durat[_wry_gr[j]] -self.oldstatus[_grp][_wry_gr[j]][1]) >(AlarmCfg['maxdurat'] *_part/2))):     #狀態超過maxpoint /4 且 maxdurat /4

                                                wry_gr.update({_grp : {_wry_gr[j] : []}})
                                                #self.oldstatus[_grp].update({_wry_gr[j] : [_count[_wry_gr[j]], _durat[_wry_gr[j]]]})
                                                self.oldstatus[_grp][_wry_gr[j]][0] = _count[(_wry_gr[j])]
                                                self.oldstatus[_grp][_wry_gr[j]][1] = _durat[(_wry_gr[j])]
                                                #print('已有舊狀態', self.oldstatus)
                                            else:   #單通道，且未達設定值1/2
                                                  pass
                                        else:   #第一次新增
                                            self.oldstatus[_grp] = {}
                                            wry_gr[_grp] = {}
                                            self.oldstatus[_grp].update({_wry_gr[j] : [_count[_wry_gr[j]], _durat[_wry_gr[j]] ,thisAlertTime]})
                                            wry_gr[_grp].update({_wry_gr[j] : []})
                                            #print('第一次新增', self.oldstatus)
                            
                #=========================================================================
            #===========================================================================
            if len(alt_gr) >0:  #所有告警群組
                _id , _name = str(len(self.thread4Calcu)).zfill(4), 'alt%s' %int(time.time())
                self.thread4Calcu.append([CalcuPhase(_id, _name, alt_gr), _id, _name])
                self.thread4Calcu[-1][0].start()
                self.thread4Calcu[-1][0].join()
                oPDStatus = self.thread4Calcu[-1][-0].PDStatus  #計算PD狀態，[0, 0],[0, 1], [1, 0], [1, 1], [0], [1]
                #print('self.thread4Calcu_alt:', self.thread4Calcu)
                self.thread4Calcu.pop(-1)
                
                for i in oPDStatus.keys():  # i == _grp
                    #oPDStatus[i][j] ~= 雙通道：[0, 0], [0, 1], [1, 1] || 單通道：[0], [1]
                    _gri = StatusBar.showgrouplnk[i][0]
                    _pdstatus = int(_tempA[_gri][-1])
                    _pdstatus = {True : lambda : hex(_pdstatus)[2:].zfill(2)[::-1],    #轉16進制併轉置
                                 False : lambda : bin(_pdstatus)[2:].zfill(2)[::-1]
                                 }.get(AlarmCfg['chx_sel'], lambda : bin(_pdstatus)[2:].zfill(2)[::-1])()
                    _pdstatus = list(_pdstatus)

                    _isAlter = sum([oPDStatus[i][j] for j in list(oPDStatus[i].keys())]) +int(AlarmCfg['chx_sel'])  #雙通道：2 +0 =2，單通道：1 +1 =2
                    for j in list(oPDStatus[i].keys()): #雙通道len(oPDStatus[i].keys()) == 2,單通道len(oPDStatus[i].keys()) == 1
                        if oPDStatus[i][j] >0:    #告警狀態 : 1
                            _pdstatus[j] = str(oPDStatus[i][j] +int(AlarmCfg['chx_sel']))   #雙通道：1，單通道：2
                        else:   #oPDStatus[i][j] == 0 不改變狀態
                            pass
                            
                    _pdstatus = ''.join(_pdstatus)
                    _pdstatus = _pdstatus[::-1] #轉置
                    _pdstatus = {True : lambda : float(int(_pdstatus, 16)),    #轉16進制
                                 False : lambda : float(int(_pdstatus, 2))
                                 }.get(AlarmCfg['chx_sel'], lambda : float(int(_pdstatus, 2)))()
                        
                    GroupSet[_gri]['oldalarstat'] = [_pdstatus, None]  #更新ChxLable用，隨即時狀態更新，會因下次運算而復歸
                    GroupSet[_gri]['mmap']['durat'].seek(-8, 2)
                    GroupSet[_gri]['mmap']['durat'].write(struct.pack('d', _pdstatus))

                    if _isAlter == 2:
                        insertHistory({i : {len(StatusBar.showgrouplnk[i][2]) :self.hist[_gri]}}, _isAlter, thisAlertTime)
                UpdateGlobals('GroupSet', GroupSet)
                pass

            if len(wry_gr) >0:  #所有警示群組
                _id , _name = str(len(self.thread4Calcu)).zfill(4), 'wry%s' %int(time.time())
                self.thread4Calcu.append([CalcuPhase(_id, _name, wry_gr), _id, _name])
                self.thread4Calcu[-1][0].start()
                self.thread4Calcu[-1][0].join()
                oPDStatus = self.thread4Calcu[-1][-0].PDStatus
                #print('self.thread4Calcu_wry:', self.thread4Calcu)
                self.thread4Calcu.pop(-1)
                #print('wry_gr:', wry_gr, 'oPDStatus:', oPDStatus)
                for i in oPDStatus.keys():  # i == _grp
                    #oPDStatus[i][j] ~= 雙通道：[0], [1] || 單通道：[0], [1]※滿足一半條件
                    _gri = StatusBar.showgrouplnk[i][0]
                    _pdstatus = int(_tempA[_gri][-1])
                    _pdstatus = {True : lambda : hex(_pdstatus)[2:].zfill(2)[::-1],    #轉16進制併轉置
                                 False : lambda : bin(_pdstatus)[2:].zfill(2)[::-1]
                                 }.get(AlarmCfg['chx_sel'], lambda : bin(_pdstatus)[2:].zfill(2)[::-1])()
                    _pdstatus = list(_pdstatus)

                    for j in list(oPDStatus[i].keys()):
                        #print('oPDStatus:', oPDStatus, 'j:', j, '_wry_gr:', _wry_gr)  #oPDStatus: {0: {1: 1}} j: 1 _wry_gr: [1]
                        #GroupSet[i]['oldalarstat'] = [oPDStatus[i][j], j]
                        if oPDStatus[i][j] >0:    #告警狀態 : 1
                            if oPDStatus[i][j] > int(_pdstatus[j]):
                                _pdstatus[j] = str(oPDStatus[i][j])   #雙通道：1，單通道：1
                            _pdstatus = ''.join(_pdstatus)  #合併
                            _pdstatus = _pdstatus[::-1] #轉置
                            _pdstatus = {True : lambda : float(int(_pdstatus, 16)),    #轉16進制
                                         False : lambda : float(int(_pdstatus, 2))
                                         }.get(AlarmCfg['chx_sel'], lambda : float(int(_pdstatus, 2)))()

                            #print(_gri, _pdstatus)
                            GroupSet[_gri]['oldalarstat'] = [_pdstatus, None]  #更新ChxLable用，隨即時狀態更新
                            GroupSet[_gri]['mmap']['durat'].seek(-8, 2)
                            GroupSet[_gri]['mmap']['durat'].write(struct.pack('d', _pdstatus))
                            print("GroupSet[%s]['oldalarstat']:" %_gri, GroupSet[_gri]['oldalarstat'])

                            try:    #含有舊狀態
                                self.oldstatus[i][j]
                                self.oldstatus[i][j][0] = self.hist[_gri]['chxpds'][j]#GroupSet[i]['chxpds'][(_wry_gr[j])]
                                self.oldstatus[i][j][1]= self.hist[_gri]['chxdurat'][j]#GroupSet[i]['chxdurat'][(_wry_gr[j])]
                                insertHistory({i : {j :self.hist[_gri]}}, oPDStatus[i][j], self.oldstatus[i][j][2])
                            except Exception as e:
                                exc_type, exc_obj, exc_tb = sys.exc_info()
                                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                                print(exc_type, fname, exc_tb.tb_lineno)
                                insertHistory({i : {j :self.hist[_gri]}}, int(oPDStatus[i][j]), thisAlertTime)
                                pass
                                
                        else:
                            pass
                UpdateGlobals('GroupSet', GroupSet)
                #for xi in list(GroupSet.keys()):
                    #print("GroupSet[%s]['oldalarstat']:" %xi, GroupSet[xi]['oldalarstat'])
                pass
            if len(rst_gr) >0:
                #Opt2ActFrm["00001"][2].resetData(rst_gr)
                #print(rst_gr)
                resetData(rst_gr)

            if len(self.thread4Calcu) >0:
                print('self.thread4Calcu:', self.thread4Calcu)
                
            if not self.stopper:
                break

    '''
    def convGri2Grp(self, gri, chx):
        j = 0
        _ch = []
        _grpA = []
        while j < len(chx):
            k = 0
            _ch.append([])
            while k < (len(GroupSet[gri]['ch']) -AlarmCfg['chx_sel']):  #自動轉換單/雙通道，單通道時要分開拿取回傳直
                _ch[j].append(chx[k +j])
                k = k+1
                if (k +j) >= len(chx):
                    break
            j = j +len(_ch[j])
        #print('_ch:', _ch)
        for _c in _ch:
            #print(_c)
            try:
                _grp = [key for key in list(StatusBar.showgrouplnk.keys()) if StatusBar.showgrouplnk[key][0] == gri and StatusBar.showgrouplnk[key][2] == _c][0]
            except:
                try:
                    _grp = [key for key in list(StatusBar.showgrouplnk.keys()) if StatusBar.showgrouplnk[key][0] == gri and all([item in StatusBar.showgrouplnk[key][2] for item in _c])][0]
                    #_grp = [key for key in list(StatusBar.showgrouplnk.keys()) if StatusBar.showgrouplnk[key][0] == gri and _c in StatusBar.showgrouplnk[key][2]][0]
                except:
                    _grp = None

            if _grp != None:
                _grpA.append(_grp)
        #print(_grpA)
        return _grpA
    '''
#=================================================================
#================ 插入歷史檔 ================================
def insertHistory(alt_grp, pdstatus, alarmtime):    #{i : {j :self.hist[_gri]}}, int(_pdstatus), thisAlertTime  #i = _grp
    global info_res,sn_var,timezone,Alert,ChxStatus,StatusBar
    global p4bee,GPIO,outpath
    global Config4Lan,AlarmCfg,History,thisSN,isMount
    StatusBar = GetGlobals('StatusBar')
    thisSN = GetGlobals('thisSN')
    outpath = GetGlobals('outpath')
    History = GetGlobals('History') #[year,mon,day,hour,min,sec,PDStatus,PDChannel,ch_i_pds,ch_i_durat......i=1~8]
    isMount = GetGlobals('isMount')
    #print(alt_grp)
    thisAlertTime = alarmtime
    alarmtime = datetime.datetime(*thisAlertTime[:6])
    pdstatus = pdstatus     #1 or 2
    #_pdstatus = {True : lambda : hex(pdstatus)[2:].zfill(2)[::-1],    #轉16進制併轉置
                 #False : lambda : bin(pdstatus)[2:].zfill(2)[::-1]
                 #}.get(AlarmCfg['chx_sel'], lambda : bin(pdstatus)[2:].zfill(2)[::-1])()
    #_pdstatus = list(_pdstatus)

    group = ''
    for key in list(StatusBar.showgrouplnk.keys()):
        group = (group +
                 (','.join(str(n) for n in StatusBar.showgrouplnk[key][3])) +';')
    
    '''
    for i in GroupSet:
        group = (group +
                 (','.join(str(n) for n in GroupSet[i]['ch'])) +';')
    #{0: {'ch': [1, 2],......}},  {1: {'ch': [3, 4],......}}, {2: {'ch': [5, 6],......}}
    '''
    
    for i in list(alt_grp.keys()):  #i == _grp
        _gri = StatusBar.showgrouplnk[i][0]
        #=========== 告警視窗 ==============

        if pdstatus == 2:
            UpdateOptStates(StatusBar, 0)
            if Alert.isTkraise != 1:
                Alert.limit = 30
                Alert.isTkraise = 1
                if bool(AlarmCfg['Ch1_LPIN']):
                    Alert.refreshIdlelbl()
            if i not in Alert.grp:
                Alert.grp.append(i)

            APM = Config4Lan.get(AlarmCfg['lang'], time.strftime("%p", thisAlertTime))
            '''
            APM = time.strftime("%p", thisAlertTime)
            APM = {
                'zh-TW' : lambda : {'AM' : lambda : '上午', 'PM' : lambda : '下午',}.get(APM, lambda : '上午')(),
                'en-US' : lambda : APM,
                }.get(AlarmCfg['lang'], lambda : {'AM' : lambda : '上午', 'PM' : lambda : '下午',}.get(APM, lambda : '上午')())()
            '''

            lodate = time.strftime("%Y/%m/%d", thisAlertTime)
            lotime = time.strftime("%I:%M:%S", thisAlertTime)
            #'AlertFrmmsgtxt : OEDGKGNHLHJENHCGCGMHIGLHHHLH'
            msgtxt = Config4Lan.get(AlarmCfg['lang'], 'OEDGKGNHLHJENHCGCGMHIGLHHHLH',
                                    vars={'para1': lodate, 'para2': APM, 'para3': lotime})
            '''
            msgtxt = {'zh-TW' : lambda : ("親愛的客戶，請注意：\n您的設備于\n" + lodate
                                          +"\n" + APM+ "  "+ lotime+"\n發生局部放電警示！"),
                      'en-US' : lambda : ("Dear Customer:\n" +
                                          "Alert!\n" +
                                          "PD occurs in HV equipment at\n" +
                                          lodate +"  " + APM+ "  "+ lotime),
                      }.get(AlarmCfg['lang'], lambda : ("親愛的客戶，請注意：\n您的設備于\n" + lodate +
                                                        "\n" + APM+ "  "+ lotime+"\n發生局部放電警示！"))()
            '''
            Alert.msgbl4Alert.config(text = msgtxt)
            Alert.tkraise()
            ChxStatus.tkraise()

            if ((AlarmCfg['alarm_type'] in (2, 3, 6, 7))):# and ('p4bee' not in globals())):
                p4bee = GetGlobals('p4bee')
                try:
                    GPIO
                    #runAler()
                    if p4bee == None:
                        #p4bee = bee(999, "p4bee", True, ('%s %s' %(lodate, lotime)), i)
                        expression = "bee%s(999, 'p4bee', True, '%s %s' , %s)" %(AlarmCfg['Ch1_LPIN'], lodate, lotime, i)
                        p4bee = eval(expression)
                        #p4bee.daemon = True
                        p4bee.start()
                        UpdateGlobals('p4bee', p4bee)
                    else:
                        p4bee.altertime = ('%s %s' %(lodate, lotime))
                        p4bee.gr = i
                        if p4bee.strtime >10:
                            p4bee.strtime = 0
                except:
                    pass
            else:
                if AlarmCfg['alarm_type'] in (4, 5, 6, 7):
                    try:
                        GPIO.output(AlarmCfg['yl_pin'], True)
                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
        else:
            if AlarmCfg['alarm_type'] in (4, 5, 6, 7):
                try:
                    GPIO.output(AlarmCfg['yl_pin'], True)
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno, 'GPIO Error.')
        #=======================================
        #=========== 輸出紀錄檔 =====================
        ## {i : {j :self.hist[_gri]}}, int(_pdstatus), thisAlertTime  #i = _grp
        _info = {}
        for item in info_res:
            _info[('Ch%s' %item[0])] = (item[1]).strip()
        mfn = (hex(int(time.mktime(thisAlertTime))))[2:]

        chxpds = ''
        chxdurat = ''
        lx = lambda s: ',' if len(s) >0 else ''
        chxpds = (chxpds + (lx(chxpds)) +
                  (','.join(str(x) for x in GroupSet[_gri]['chxpds'])))    #len = (通道數/群) +1
        chxdurat = (chxdurat + (lx(chxdurat)) +
                    (','.join(('%.2f' %x) for x in GroupSet[_gri]['chxdurat'])))   #len = (通道數/群) +1
        #print(chxpds, chxdurat)
        for j in list(alt_grp[i].keys()):   #i == _grp
            #雙通道時，j == len(StatusBar.showgrouplnk[i][2])；單通道時，j == 0 or 1
            #=================== update historyX.~ ====================
            _h0 = struct.unpack('I' *33, History[0][:])
            if _h0[0] != 0:
                History[1].seek(0)
                float_array = array('I', _h0)   #[year,mon,day,hour,min,sec,PDStatus,PDGroup,PDChannel,ch_i_pds,ch_i_durat,ch_i_mv,......i=1~8]
                float_array.tofile(History[1])
            _tmary = list(thisAlertTime[:6])
            _tmary.append(pdstatus)
            #_tmary.append(_gri)
            _tmary.append(i)
            _tmary.append(j)
            #print(alt_grp[i][j]['_tempA'])
            for _ti in alt_grp[i][j]['_tempA']:     #_tempA : chxpds, chxdurat, mv, lasttime, chxinittime  *3, PDStatus
                _s = list(alt_grp[i][j]['_tempA'][_ti][:6])     #_ti = [i in GroupSet]
                _s = [ abs(item) for item in _s]    #注意，ＤＥＭＯ箱有機會因取樣時間設太短，造成持續時間為負（效能不佳的系統較可能發生）
                [_tmary.append(_is) for _is in _s]
            _tmary = list(map(int, _tmary)) #轉成整數，以備modbus傳輸
            History[0].seek(0)
            #print(len(History[0]), 'len(_tmary):', len(_tmary), '_tmary:', *_tmary)
            History[0].write(struct.pack('%sI' %len(_tmary), *_tmary))
            
            #==================================================
            #=========== Output File ===============================
            if isMount:
                try:
                    pddfile = open((outpath + ('//%s.hist' %thisSN) +('//%s_g%s(%s).hist' %(mfn, i, j))),"wb+")
                    #print([time.mktime(thisAlertTime)])
                    
                    #pddfile.write('<<<'.encode('ascii'))
                    pddfile.write((GetGlobals('thisSN') +'###').encode('ascii'))
                    pddfile.write(('%.1f###' %AlarmCfg['reffreq']).encode('ascii'))
                    pddfile.write((timezone +'###' ).encode('ascii'))
                    pddfile.write(('%s###' %AlarmCfg['maxpoint']).encode('ascii'))
                    pddfile.write(('%.1f###' %AlarmCfg['maxdurat']).encode('ascii'))
                    pddfile.write(('%s###' %AlarmCfg['sync']).encode('ascii'))
                    pddfile.write(('%s###' %AlarmCfg['demo']).encode('ascii'))
                    pddfile.write((group +'###').encode('ascii'))
                    pddfile.write(('%s###' %AlarmCfg['ch1_sensor']).encode('ascii'))
                    pddfile.write(('%.1f###' %AlarmCfg['ch1_triv']).encode('ascii'))
                    pddfile.write(('%s###' %AlarmCfg['ch2_sensor']).encode('ascii'))
                    pddfile.write(('%.1f###' %AlarmCfg['ch2_triv']).encode('ascii'))
                    pddfile.write(('%s###' %AlarmCfg['ch3_sensor']).encode('ascii'))
                    pddfile.write(('%.1f###' %AlarmCfg['ch3_triv']).encode('ascii'))
                    pddfile.write(('%s###' %AlarmCfg['ch4_sensor']).encode('ascii'))
                    pddfile.write(('%.1f' %AlarmCfg['ch4_triv']).encode('ascii'))
                    #pddfile.write(('<<<').encode('ascii'))
                    pddfile.write(('\n').encode('ascii'))
                    
                    float_array = array('d', [time.mktime(thisAlertTime)])                           #len = 1 *8
                    float_array.tofile(pddfile)
                    float_array = array('B', [pdstatus])                           #len = 1 *1
                    float_array.tofile(pddfile)
                    float_array = array('B', [i])                           #len = 1 *1 告警群組
                    float_array.tofile(pddfile)
                    float_array = array('B', [j])                           #len = 1 *1 告警通道
                    float_array.tofile(pddfile)
                    float_array.tofile(pddfile)
                    #float_array = array('L', alt_grp[i][j]['chxpds'])                           #len = len(alt_grp[i][j]['chxpds']) *4 數量
                    float_array = array('L', [int(item) for item in alt_grp[i][j]['chxpds']])                           #len = len(alt_grp[i][j]['chxpds']) *4 數量((通道數/群) +1)
                    float_array.tofile(pddfile)
                    float_array = array('d', alt_grp[i][j]['chxdurat'])                           #len = len(alt_grp[i][j]['chxpds']) *8 延續((通道數/群) +1)
                    float_array.tofile(pddfile)
                    pddfile.write(alt_grp[i][j]['cmdline']) #len = 9
                    for k in list(alt_grp[i][j]['data4main'].keys()):
                        nrec = len(alt_grp[i][j]['data4main'][k]['y'])
                        float_array = array('L', [nrec])                           #len = 1 *4
                        float_array.tofile(pddfile)
                        float_array = array('f', alt_grp[i][j]['data4main'][k]['x'])                           #len = nrec *4
                        float_array.tofile(pddfile)
                        float_array = array('f', alt_grp[i][j]['data4main'][k]['y'])                           #len = nrec *4
                        float_array.tofile(pddfile)
                    for k in list(alt_grp[i][j]['data4twmp'].keys()):
                        nrec = len(alt_grp[i][j]['data4twmp'][k]['y'])
                        float_array = array('L', [nrec])                           #len = 1 *4
                        float_array.tofile(pddfile)
                        float_array = array('f', alt_grp[i][j]['data4twmp'][k]['x'])                           #len = nrec *4
                        float_array.tofile(pddfile)
                        float_array = array('f', alt_grp[i][j]['data4twmp'][k]['y'])                           #len = nrec *4
                        float_array.tofile(pddfile)
                    pddfile.close()
                    #===================================================================
                    #============================== 更新資料庫 ==============================

                    db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
                    db.execute("PRAGMA journal_mode=WAL")
                    cursor  = db.cursor()
                    cursor.execute("select * from history where alarmtime = ? and pdchx = ?", (alarmtime,i, ))
                    hs = cursor.fetchone()
                    if hs is None:      #新增
                        cursor.execute("select count(*) as count from history")
                        sn = cursor.fetchone()[0] +1
                        cursor.execute("insert into history (sn, chxpds, chxdurat, "+
                                       "pdchx, pdstatus, alarmtime, linkfile) "+
                                       "values (?, ?, ?, ?, ?, ?, ?)",
                                       (sn, chxpds, chxdurat, i, pdstatus, alarmtime, ('%s_g%s(%s).hist' %(mfn, i, j))))
                    else:               #更新
                        sn = hs[0]
                        cursor.execute("update history set chxpds =?, chxdurat =? "+
                                       "where sn =?", (chxpds, chxdurat, sn,))

                    db.commit()
                    cursor.close()
                    db.close()
                    del db, cursor, sn, hs
                except:
                    pass
            #==================================================
        del chxpds, chxdurat, lx

        #=======================================================================
#=======================================================
#======================= WebView Windows ======================
'''
class WebViewForm(tk.Toplevel):
    def __init__(self, parent, info):
        global curPath,root
        tk.Toplevel.__init__(self, parent)
        self.info = info
        self.icon = tk.PhotoImage( file = (curPath +'//link.png'))
        self.attributes("-topmost", 1) #最上層顯示
        self.title('WebView')

        self.tk.call('wm', 'iconphoto', self._w, self.icon)
        self.configure(background='#ffffff', takefocus = True, bd = 0)    #背景顏色

        size = (root.winfo_width(), root.winfo_height())
        left = root.winfo_x()
        top = root.winfo_y()
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))

        if thisOS == 'Linux' :
            self.attributes('-fullscreen', True)    #全螢幕
            
        self.resizable(width = False, height = False)    #可否變更大小
        self.protocol("WM_DELETE_WINDOW", self.on_exit)    #重新導向 Close Even
        self.transient(parent)
        self.name = None

        frame2=WebView2(self, 770, 480)
        frame2.load_url('http://192.168.1.31')
        frame2.pack()

        self.icon4exit = tk.PhotoImage(file = (curPath +"//Error.png"))
        self.exitbtn = tk.Button(self, image = self.icon4exit, bg = '#ffffff',
                                 relief = tk.FLAT, command = self.on_exit)
        self.exitbtn.place(x = 730, y = 0)

    def on_exit(self):
        self.destroy()
        PopGlobals(self.name)
'''
#=======================================================
#======================= HistScreen Windows ======================
class HistScreen(tk.Toplevel):
    def __init__(self, parent, info):
        global curPath,root,AlarmCfg
        global Ch_Status
        tk.Toplevel.__init__(self, parent)
        self.info = info
        #print('self.info:', self.info)
        #self.info: [['sn', 6], ['pdchx', 1], ['pdstatus', 1], ['alarmtime', '2021-03-11 14:33:28'], ['chxpds', '33.0,25.0,118.0'], ['chxdurat', '15.46,44.45,187.75'], ['linkfile', '6049b9b8_g1(1).hist']]
        self.datachk = False
        self.icon = tk.PhotoImage( file = (curPath +'//garea.png'))
        self.attributes("-topmost", 1) #最上層顯示
        self.title('History Reload')
        '''
        {
            'zh-TW' : lambda : self.title('資料回調'),
            'en-US' : lambda : self.title('History Reload'),
            }.get(AlarmCfg['lang'], lambda : self.title('資料回調'))()
        '''
        self.tk.call('wm', 'iconphoto', self._w, self.icon)
        self.configure(background='#ffffff', takefocus = True, bd = 0)    #背景顏色

        size = (root.winfo_width(), root.winfo_height())
        left = root.winfo_x()
        top = root.winfo_y()
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))

        if thisOS == 'Linux' :
            self.attributes('-fullscreen', True)    #全螢幕
            
        self.resizable(width = False, height = False)    #可否變更大小
        self.protocol("WM_DELETE_WINDOW", self.on_exit)    #重新導向 Close Even
        self.transient(parent)
        self.name = None
        #============================ Get Parameters =====================================
        '''
        db = sqlite3.connect(dbpath, timeout=5.0)	#連接資料庫
        db.execute("PRAGMA journal_mode=WAL")
        cursor  = db.cursor()
        cursor.execute("select * from group_setting")
        gpset_res = cursor.fetchall()
        db.commit()
        cursor.close()
        db.close()
        '''
        self.linkfile = ([x for x in self.info if 'linkfile' in x][0][1])   #*.hist
        _basename = (os.path.splitext(os.path.basename(self.linkfile))[0])
        #print(_basename) #5ceba9a9_g0(0)
        #=================================================================================
        self.viewGP = 0
        self.loaddata()

        self.icon4exit = tk.PhotoImage(file = (curPath +"//Error.png"))
        self.exitbtn = tk.Button(self, image = self.icon4exit, bg = '#ffffff',
                                 relief = tk.FLAT, command = self.on_exit)
        self.exitbtn.place(x = 730, y = 0)

        if self.datachk:
            self.mainfrm = HistScr4MainFrm(self)
            self.mainfrm.tkraise()
            self.exitbtn.tkraise()
        else:
            self.on_exit()

    def loaddata(self):
        global curPath,showerrorFrm,thisSN,outpath
        thisSN = GetGlobals('thisSN')
        outpath = GetGlobals('outpath')
        pddfile = open((outpath +('//%s.hist' %thisSN) +("//%s" %self.linkfile)), "rb")
        ## structure : BFEBFBFF000406E3###60.0###Asia/Taipei###20###30###1###0###1,2;###2###1200.0###4###1200.0###2###1200.0###4###1200.0
        line = (pddfile.readline().decode('ascii')).split('###')
        #line : ['BFEBFBFF000406E3', '60.0', 'Asia/Taipei', '30', '20.0', '1', '99', '1;2;', '2', '1200.0', '4', '1200.0', '2', '1200.0', '4', '1200.0\n']
        #sn,refreq,timezone,maxpoint,maxdurat,sync,demo,group,......
        #print(line)
        self.Config = {}
        self.GroupSet = {}

        try:
            self.Config['SN'] = line[0]
            self.Config['reffreq'] = line[1]
            self.Config['timezone'] = line[2]
            self.Config['maxpoint'] = int(line[3])
            self.Config['maxdurat'] = float(line[4])
            self.Config['sync'] = line[5]
            self.Config['demo'] = line[6]
            self.Config['group'] = line[7].split(';')
            self.Config['group'] = [item.strip() for item in self.Config['group']]
            self.Config['group'] = [item for item in self.Config['group'] if len(item) >0]  #self.Config['group'] == ['1,2', '3,4', '5,6']
            #print('self.Config:', self.Config)
            #self.Config: {'SN': 'BFEBFBFF000406E3', 'reffreq': '60.0', 'timezone': 'Asia/Taipei', 'maxpoint': 30, 'maxdurat': 20.0, 'sync': '1', 'demo': '99', 'group': ['1', '2']}
            ##self.Config['group'] = ['1,2', '3,4', '5,6']    _ch = [[1,2], [3,4], [5,6]] self.maxch4grp = 2
            ##self.Config['group'] = ['1', '2', '3', '4', '5', '6']    _ch = [[1], [2], [3], [4], [5], [6]] self.maxch4grp = 1

            self._maxch4grp = 2	    #預設雙通道
            self.maxch4grp = 1
            for i in range(0, len(self.Config['group'])):
                _ch = [int(x) for x in self.Config['group'][i].split(',')]
                if len(_ch) > self.maxch4grp:
                    self.maxch4grp = len(_ch)
                #print('_ch:', _ch)  #[1], [2]
                #print('self.Config["group"]:', self.Config['group'][i], '_ch:', _ch)    #雙通道 self.Config["group"]: 1,2 _ch: [1, 2]
                #單通道 self.Config["group"]: 1 _ch: [1]
                #           self.Config["group"]: 2 _ch: [2]
                self.GroupSet[i] = {'ch': _ch}
                self.GroupSet[i]['durat'] = []
                self.GroupSet[i]['count'] = []
                self.GroupSet[i]['sensor'] = []
                self.GroupSet[i]['triv'] = []
                self.GroupSet[i]['info'] = {}
                [self.GroupSet[i]['triv'].append('') for ii in range(0, self._maxch4grp)]    #len(self.GroupSet[i]['triv']) == 2

            _r = pddfile.read(8)
            self.alarmtime = struct.unpack('d', _r[:8])[0]    #time.time()
            self.alarmtime = datetime.datetime.fromtimestamp(self.alarmtime).strftime('%Y/%m/%d %H:%M:%S')

            _r = pddfile.read(1)
            self.pdstatus = struct.unpack('B', _r[:])[0]
            
            _r = pddfile.read(1)
            self.alert_group = struct.unpack('B', _r[:])[0]
            
            _r = pddfile.read(1)
            self.alert_ch = struct.unpack('B', _r[:])[0]
            #print(self.pdstatus, self.alert_group, self.alert_ch)
            _r = pddfile.read(4 )
            _s = hex(struct.unpack('L' , _r[:])[0]) #0x24
            #_s = _s[2:].zfill(len(self.GroupSet[i]['ch']))
            _s = _s[2:].zfill(self._maxch4grp)
            while len(_s) >0:
                self.GroupSet[self.alert_group]['sensor'].append(int(_s[0], 16))
                _s = _s[1:]
            #print("self.GroupSet[i]['sensor']:", self.GroupSet[i]['sensor'])    #self.GroupSet[i]['sensor']: [2, 4]
                
            #_r = pddfile.read(4 *self.maxch4grp)
            #self.GroupSet[i]['count'] = struct.unpack('L' *self.maxch4grp, _r[:])
            #self.maxpoint = struct.unpack('L' *self.maxch4grp, _r[:])
            _r = pddfile.read(4 *(self._maxch4grp +1))
            self.GroupSet[self.alert_group]['count'] = struct.unpack('L' *(self._maxch4grp +1), _r[:])
            
            #_r = pddfile.read(8 *self.maxch4grp)
            #self.GroupSet[viewGP]['durat'] = struct.unpack('d' *self.maxch4grp, _r[:])
            #self.maxdurat = struct.unpack('d' *self.maxch4grp, _r[:])
            _r = pddfile.read(8 *(self._maxch4grp +1))
            #self.GroupSet[viewGP]['durat'] = struct.unpack('d' *(self.maxch4grp +1), _r[:])
            self.GroupSet[self.alert_group]['durat'] = struct.unpack('d' *(self._maxch4grp +1), _r[:])
            
            _r = pddfile.read(9)
            self.cmdline = _r.hex() #10610101010102007e
            #print('_r:', _r, 'self.cmdline:', self.cmdline)
            self.Config['trig_ch'] = [int(self.cmdline[0 : 1]) ,int(self.cmdline[1 : 2])]   #self.Config['trig_ch'] == [1, 0]
            self.Config['trig_ch'] = [idx for idx in range(0, len(self.Config['trig_ch'])) if self.Config['trig_ch'][idx] == 1][0]  #self.Config['trig_ch'] == 0

            self.Config['trig_lv'] = int(self.cmdline[2 : 4], 16)
            #self.Config['trig_lv'] = math.modf(abs((self.Config['trig_lv'] *7.6) -741.7 +4.5))[1]  #shift = -4.5
            self.Config['trig_lv'] = math.modf(abs((self.Config['trig_lv'] *7.6) -741.7))[1]
            self.Config['trig_lv'] = '%.1f' %(self.Config['trig_lv'])   #self.Config['trig_lv'] = =193.0
            #print("len(self.GroupSet[self.viewGP]['triv']):", len(self.GroupSet[self.viewGP]['triv']))
            self.GroupSet[self.alert_group]['triv'][self.Config['trig_ch']] = self.Config['trig_lv']
            self.Config['wave_out'] = int(self.cmdline[4 : 6], 16)
            self.Config['fft_out'] = int(self.cmdline[6 : 8], 16)
            self.Config['prpd_out'] = int(self.cmdline[8 : 10], 16)
            self.Config['twmap_out'] = int(self.cmdline[10 : 12], 16)
            self.Config['sync_opt'] = int(self.cmdline[12 : 14], 16)
            self.Config['list_choose'] = int(self.cmdline[14 : 16], 16)
            self.Config['gain'] = (bin(int(self.cmdline[16 : 18], 16))[2:]).zfill(8)
            #print(self.cmdline[16 : 18], int(self.cmdline[16 : 18], 16), (bin(int(self.cmdline[16 : 18], 16))[2:]),(bin(int(self.cmdline[16 : 18], 16))[2:]).zfill(8))
            #7e 126 1111110 01111110
            
            self.Data = {}

            for key in ['data4main', 'data4twmp']:
                self.Data[key] = {}
                for k in range(0, self._maxch4grp):

                    self.Data[key][k] = {}
                    
                    _r = pddfile.read(4)
                    self.Data[key][k]['counters'] = struct.unpack('L', _r)[0]
                    #print(self.Data[key][k]['counters'])
                    
                    _r = pddfile.read(4 *self.Data[key][k]['counters'])
                    self.Data[key][k]['x'] = struct.unpack('f' *self.Data[key][k]['counters'], _r)
                    self.Data[key][k]['x'] = [self.Data[key][k]['x'][item] for item in list(range(0, len(self.Data[key][k]['x'])))
                                              if self.Data[key][k]['x'][item] != 65535.0]
                    
                    _r = pddfile.read(4 *self.Data[key][k]['counters'])
                    self.Data[key][k]['y'] = struct.unpack('f' *self.Data[key][k]['counters'], _r)
                    self.Data[key][k]['y'] = [self.Data[key][k]['y'][item] for item in list(range(0, len(self.Data[key][k]['y'])))
                                              if self.Data[key][k]['y'][item] != 65535.0]

            self.datachk = True
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            #'loaddataErr_til : DGAGOGLGLGOGLHOGKENHNHAFLHGGDG'
            #'loaddataErr_txt : DGAGOGLGLGOGLHOGKENHNHAFLHHHLH'
            til, txt = (Config4Lan.get(AlarmCfg['lang'], 'DGAGOGLGLGOGLHOGKENHNHAFLHGGDG'),
                        Config4Lan.get(AlarmCfg['lang'], 'DGAGOGLGLGOGLHOGKENHNHAFLHHHLH'))
            '''
            til, txt = (
                {
                    'zh-TW' : lambda : ("訊息", "檔案格式錯誤\n"),
                    'en-US' : lambda : ("Information", "File format error\n"),
                    }.get(AlarmCfg['lang'], lambda : ("訊息", "檔案格式錯誤\n"))())
            '''
            #tkmsgbox.showerror(til, txt, parent = self)

            showerrorFrm = GetGlobals('showerrorFrm')
            showerrorFrm.msg_var.set(txt)
            showerrorFrm.updatepos('err')
            showerrorFrm.tkraise()
            pass
        
        pddfile.close()
        
    def on_exit(self):
        self.destroy()
        PopGlobals(self.name)

#=======================================================================
#============ class HistScr4demo_MainFrm(tk.Frame) ============================================
class HistScr4MainFrm(tk.Frame):
    def __init__(self, parent):
        global curPath,AlarmCfg,GroupSet,sensors,sensorOption,figDpi,Config4Lan,viewGP
        tk.Frame.__init__(self, parent)
        self.parent = parent
        viewGP = GetGlobals('viewGP')
        self.config(relief = tk.GROOVE, bg = '#ffffff',
                    width = 770,
                    height = 480)
        self.place(x = 0, y = 0)
        self.path4main = {}
        self.path4legend = []
        #====================== 參數區 ========================
        #figDpi = 72.0
        figH = self['height']/ figDpi
        figW = self['width'] / figDpi
        self.fig4main = Figure(figsize = (figW, figH), dpi = figDpi, facecolor='#ffffff')
        #====================== 圖表區 ========================
        axL = ((60 * (figDpi/72))/self['width']) *1.5
        axR = ((20 * (figDpi/72))/self['width']) *12.5
        axB = ((85 * (figDpi/72))/self['height']) *1.1
        axT = (100 * (figDpi/72))/self['height']
        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        self.ax4main = self.fig4main.add_axes(axSize)  #left, bottom, width, height

        axL = ((60 * (figDpi/72))/self['width']) *9.9
        axR = ((20 * (figDpi/72))/self['width']) *0.4
        axB = ((85 * (figDpi/72))/self['height']) *1.1
        axT = ((100 * (figDpi/72))/self['height']) *2.0
        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]
        self.ax4twmap = self.fig4main.add_axes(axSize)  #left, bottom, width, height
        
        self.def_til_font = FontProperties(fname = (rawS(curPath + '//msjhbd.ttc')))
        self.def_til_font.set_size(math.ceil(18*72/figDpi))
        self.def_til_font.set_weight('bold')
        #'ax4main_til = OGHHLDCGOGGGBGAFLHGGDG'
        self.ax4main.set_title(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGAFLHGGDG'),
                               fontproperties = self.def_til_font, loc='left')
        self.ax4twmap.set_title(Config4Lan.get(AlarmCfg['lang'], 'TF map'),
                                fontproperties = self.def_til_font, loc='left')

        self.def_til_font = FontProperties(fname = (rawS(curPath + '//wqy-zenhei.ttc')))
        self.def_til_font.set_size(math.ceil(15*72/figDpi))
        self.def_til_font.set_weight('normal')

        #'ax4mainXlbl = OGHHLDCGOGGGBGHFDGNGDG
        #'ax4mainYlbl = OGHHLDCGOGGGBGGFDGNGDG
        self.ax4main.set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGHFDGNGDG'),
                                fontproperties = self.def_til_font)
        self.ax4main.set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGGFDGNGDG'),
                                fontproperties = self.def_til_font)
        self.ax4twmap.set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'Equivalent Frequence'), fontproperties = self.def_til_font)
        self.ax4twmap.set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'Equivalent Timelength'), fontproperties = self.def_til_font)

        self.path4phas = Line2D([], [], color = "#000000", linestyle = '--', linewidth = 1)

        self.ax4main.add_line(self.path4phas)

        self.ang = list(range(0, 361,5))
        self.amp = [math.sin(math.radians(_a)) for _a in self.ang]
        self.path4phas.set_data(self.ang, self.amp)

        self.canvas4main = FigureCanvasTkAgg(self.fig4main, self)
        #============================== Information Axia ==========================
        axL = (150 * (figDpi/72))/self['width']
        axR = (20 * (figDpi/72))/self['width']
        axB = (390 * (figDpi/72))/self['height'] 
        axT = (0 * (figDpi/72))/self['height']
        axW = 1 - axL - axR
        axH = 1 - axT - axB
        axSize = [axL, axB, axW, axH]

        self.InfoAx = self.fig4main.add_axes(axSize)
        self.InfoAx.axis('off')
        self.InfoAx.set_navigate(False)

        #================= 告警時間 ==================
        self.def_til_font.set_size(math.ceil(14*72/figDpi))
        self.InfoAx.add_patch(
            matplotlib.patches.Rectangle(
                (0.01, 0.59),   # (x,y)
                0.26,          # width
                0.249,          # height
                fill = False
                )
            )
        lbltext = Config4Lan.get(AlarmCfg['lang'], 'AlarmTime')
        self.InfoAx.text(0.025, 0.908, lbltext,
                         ha='left', va='top',
                         fontproperties = self.def_til_font,
                         backgroundcolor = '#ffffff')
        self.alarm_txt = self.InfoAx.text(0.025, 0.72, self.parent.alarmtime,
                                          ha='left', va='top',
                                          fontproperties = self.def_til_font,
                                          backgroundcolor = 'none',
                                          color = '#0000ff')
        #=============================================
        #================= 告警等級 ==================
        self.InfoAx.add_patch(
            matplotlib.patches.Rectangle(
                (0.01, 0.212),   # (x,y)
                0.13,          # width
                0.249,          # height
                fill=False
                )
            )
        lbltext = Config4Lan.get(AlarmCfg['lang'], 'PDLev')
        self.InfoAx.text(0.025, 0.53, lbltext,
                         ha='left', va='top',
                         fontproperties = self.def_til_font,
                         backgroundcolor = '#ffffff')
        #print('self.parent.pdstatus:', self.parent.pdstatus)
        if int(self.parent.pdstatus) >1:
            _fg = '#ff0000'
        else:
            _fg = '#ff9600'
        self.pdstatus_txt = self.InfoAx.text(0.025, 0.342, self.parent.pdstatus,
                                             ha='left', va='top',
                                             fontproperties = self.def_til_font,
                                             backgroundcolor = 'none',
                                             color = _fg)
        #=============================================
        #================= 工作頻率 ==================
        self.InfoAx.add_patch(
            matplotlib.patches.Rectangle(
                (0.14, 0.212),   # (x,y)
                0.13,          # width
                0.249,          # height
                fill=False
                )
            )
        lbltext = Config4Lan.get(AlarmCfg['lang'], 'SyncFreq')

        self.InfoAx.text(0.155, 0.53, lbltext,
                         ha='left', va='top',
                         fontproperties = self.def_til_font,
                         backgroundcolor = '#ffffff')
        self.reffreq_txt = self.InfoAx.text(0.164, 0.342, self.parent.Config['reffreq'],
                                            ha='left', va='top',
                                            fontproperties = self.def_til_font,
                                            backgroundcolor = 'none',
                                            color = '#0000ff')
        self.InfoAx.text(0.245, 0.342, 'Hz',
                         ha='left', va='top',
                         fontproperties = self.def_til_font,
                         backgroundcolor = 'none',
                         color = '#000000')
        
        #================= 通道訊息與繪圖 ==================
        self.prpd4main = []
        self.twmap4main = []
        self.chinfo4hist = {}
        self.chtil4hist = {}
        _gri = int(self.parent.alert_group /2)
        for i in range(0, len(self.parent.GroupSet[self.parent.alert_group]['ch'])):
            _ch = self.parent.GroupSet[self.parent.alert_group]['ch'][i]
            _grj = int(not (_ch %2))
            lbltext = ('%s %s' %(Config4Lan.get(AlarmCfg['lang'], 'channel'), _ch))
            
            self.prpd4main.append(self.ax4main.plot([], [], 'o', ms = 5.0,
                                                    color = prpd4main[i +1][0].get_color(),
                                                    label = lbltext))
            
            self.twmap4main.append(self.ax4twmap.plot([], [], 'o', ms = 5.0,
                                                      color = prpd4main[i +1][0].get_color(),
                                                      label = lbltext))

            self.prpd4main[i][0].set_data(self.parent.Data['data4main'][i]['x'], self.parent.Data['data4main'][i]['y'])
            self.twmap4main[i][0].set_data(self.parent.Data['data4twmp'][i]['x'], self.parent.Data['data4twmp'][i]['y'])
            
            if len(self.parent.Data['data4main'][i]['y']) >0:   #一通道為空(未觸發)時出錯
                maxA = math.ceil(max([abs(self.parent.Data['data4main'][i]['y'][_i]) for _i in range(0, len(self.parent.Data['data4main'][i]['y']))]))
            else:
                maxA = 0

            if maxA >= max(self.amp):
                self.amp = [math.sin(math.radians(_a)) *maxA for _a in self.ang]
                self.path4phas.set_data(self.ang, self.amp)
            
            self.chtil4hist[i] = {}
            self.chinfo4hist[i] = {}
            self.chinfo4hist[i]['Frame'] = self.InfoAx.add_patch(
                matplotlib.patches.Rectangle(
                    (((i *0.34) +0.28), 0.008),   # (x,y)
                    0.33,          # width
                    0.82,          # height
                    fill=False,
                    linewidth = 1.0,
                    color = '#000000'
                    )
                )

            self.chinfo4hist[i]['chlbl'] = self.InfoAx.text(((i *0.34) +0.295), 0.908, '',
                                                            ha='left', va='top',
                                                            fontproperties = self.def_til_font,
                                                            backgroundcolor = '#ffffff')
            self.chinfo4hist[i]['chlbl'].set_text(lbltext)
            
            lbltext = Config4Lan.get(AlarmCfg['lang'], 'Lev')
            self.chtil4hist[i]['triv'] = self.InfoAx.text(((i *0.34) +0.375), 0.789, lbltext,
                                                  ha='left', va='top',
                                                  fontproperties = self.def_til_font,
                                                  backgroundcolor = 'none')
            
            lbltext = Config4Lan.get(AlarmCfg['lang'], 'mV.')
            self.chtil4hist[i]['mV'] = self.InfoAx.text(((i *0.34) +0.560), 0.789, lbltext,
                                                          ha='left', va='top',
                                                          fontproperties = self.def_til_font,
                                                          backgroundcolor = 'none')
            
            lbltext = Config4Lan.get(AlarmCfg['lang'], 'Count.')
            self.chtil4hist[i]['count'] = self.InfoAx.text(((i *0.34) +0.375), 0.602, lbltext,
                                                          ha='left', va='top',
                                                          fontproperties = self.def_til_font,
                                                          backgroundcolor = 'none')
            
            lbltext = Config4Lan.get(AlarmCfg['lang'], 'Durat.')
            self.chtil4hist[i]['durat'] = self.InfoAx.text(((i *0.34) +0.375), 0.415, lbltext,
                                                          ha='left', va='top',
                                                          fontproperties = self.def_til_font,
                                                          backgroundcolor = 'none')
            
            #'SecLbl = MFKGMGDENGDG
            lbltext = Config4Lan.get(AlarmCfg['lang'], 'MFKGMGDENGDG')
            self.chtil4hist[i]['sec'] = self.InfoAx.text(((i *0.34) +0.560), 0.415, lbltext,
                                                          ha='left', va='top',
                                                          fontproperties = self.def_til_font,
                                                          backgroundcolor = 'none')


            self.chinfo4hist[i]['triv_txt'] = self.InfoAx.text(((i *0.34) +0.440), 0.789,
                                                               '',
                                                               ha='left', va='top',
                                                               fontproperties = self.def_til_font,
                                                               backgroundcolor = 'none',
                                                               color = '#0000ff')

            self.chinfo4hist[i]['count_txt'] = self.InfoAx.text(((i *0.34) +0.440), 0.602, '',
                                                                ha='left', va='top',
                                                                fontproperties = self.def_til_font,
                                                                backgroundcolor = 'none',
                                                                color = '#0000ff')
            self.chinfo4hist[i]['durat_txt'] = self.InfoAx.text(((i *0.34) +0.440), 0.415,
                                                                '',
                                                                ha='left', va='top',
                                                                fontproperties = self.def_til_font,
                                                                backgroundcolor = 'none',
                                                                color = '#0000ff')

            self.chinfo4hist[i]['info'] = self.InfoAx.text(((i *0.34) +0.295), 0.228,
                                                           '',
                                                           ha='left', va='top',
                                                           fontproperties = self.def_til_font,
                                                           backgroundcolor = 'none',
                                                           color = '#0000ff')

            _triv = self.parent.GroupSet[(self.parent.alert_group)]['triv'][_grj]
            _dt = self.parent.GroupSet[(self.parent.alert_group)]['durat'][_grj]
            if _dt > 0:
                _dt = ('%.2f' %self.parent.GroupSet[(self.parent.alert_group)]['durat'][_grj])
            else:
                _dt = ''
            _cs = self.parent.GroupSet[(self.parent.alert_group)]['count'][_grj]
            if _cs > 0:
                _cs = ('%d' %self.parent.GroupSet[self.parent.alert_group]['count'][_grj])
            else:
                _cs = ''
            try:
                self.chinfo4hist[i]['senImg'].remove()
            except Exception as e:
                pass
            try:
                sensor = int(self.parent.GroupSet[self.parent.alert_group]['sensor'][_grj])
                fn = get_sample_data((curPath + "//" + sensors[sensorOption[sensor]][1]),
                                     asfileobj = False)
                arr_img = plt.imread(fn, format = 'png')
                imagebox = OffsetImage(arr_img, zoom = 0.60)
                imagebox.image.axes = self.InfoAx
                self.chinfo4hist[i]['senImg'] = AnnotationBbox(imagebox, [((i *0.34) +0.33), 0.525],
                                                               bboxprops =dict(facecolor = 'none',
                                                                               edgecolor = 'none'))
                self.InfoAx.add_artist(self.chinfo4hist[i]['senImg'])
            except Exception as e:
                pass


            self.chinfo4hist[i]['triv_txt'].set_text(_triv)
            self.chinfo4hist[i]['count_txt'].set_text(_cs)
            self.chinfo4hist[i]['durat_txt'].set_text(_dt)

            if int(self.parent.pdstatus) >1:
                self.chinfo4hist[i]['Frame'].set_color(vars(self.pdstatus_txt)['_color'])
                self.chinfo4hist[i]['Frame'].set_linewidth(2.0)
            elif _grj == self.parent.alert_ch:
                self.chinfo4hist[i]['Frame'].set_color(vars(self.pdstatus_txt)['_color'])
                self.chinfo4hist[i]['Frame'].set_linewidth(2.0)
        #=============================================

        self.def_til_font.set_size(math.ceil(10*72/figDpi))
        self.ax4main.legend(prop = self.def_til_font, loc = 2)
        self.ax4twmap.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
        self.def_til_font.set_size(math.ceil(12*72/figDpi))
        [label.set_fontproperties(self.def_til_font) for label in self.ax4twmap.get_xticklabels()]
        [label.set_fontproperties(self.def_til_font) for label in self.ax4twmap.get_yticklabels()]
        self.ax4main.grid()
        self.ax4twmap.grid()

        self.ax4main.set_autoscaley_on(True)
        self.ax4twmap.set_autoscaley_on(True)
        self.ax4main.set_xlim([0, 360])
        self.ax4main.set_xticks(list(range(0, 361, 30)))

        self.ax4main.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
        self.def_til_font.set_size(math.ceil(14*72/figDpi))
        [label.set_fontproperties(self.def_til_font) for label in self.ax4main.get_xticklabels()]
        [label.set_fontproperties(self.def_til_font) for label in self.ax4main.get_yticklabels()]

        self.ax4main.relim()
        self.ax4main.autoscale_view()
        self.ax4twmap.relim()
        self.ax4twmap.autoscale_view()
        self.fig4main.canvas.draw()
        self.fig4main.canvas.flush_events()
        #==========================================================================
        self.toolbar4main = CustomToolbar(self.canvas4main, self)
        self.toolbar4main.config(bg = "#ffffff")
        #========================================================================
        self.toolbar4main.place(x = 0,
                                y = self['height'] -self.toolbar4main.winfo_reqheight()-10)
        self.canvas4main.get_tk_widget().place(x = 0, y = 0)
        self.canvas4main._tkcanvas.place(x = 0, y = 0)

        #==========================================================================
        self.def_til_font.set_size(math.ceil(20*72/self.fig4main.dpi))
        #'ax4main_til = OGHHLDCGOGGGBGAFLHGGDG'
        self.ax4main.set_title(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGAFLHGGDG'),
                               fontproperties = self.def_til_font, loc='left')
        self.ax4twmap.set_title(Config4Lan.get(AlarmCfg['lang'], 'TF map'),
                                fontproperties = self.def_til_font, loc='left')
        
        self.def_til_font.set_size(math.ceil(16*72/self.fig4main.dpi))
        self.ax4main.set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGHFDGNGDG'),
                                fontproperties = self.def_til_font)
        self.ax4main.set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGGFDGNGDG'),
                                fontproperties = self.def_til_font)
        self.ax4twmap.set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'Equivalent Frequence'),
                                 fontproperties = self.def_til_font)
        self.ax4twmap.set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'Equivalent Timelength'),
                                 fontproperties = self.def_til_font)
        #self.change_lbl()
        #self.drawchart()

    '''
    def change_lbl(self):
        global AlarmCfg,curPath,sensors,sensorOption
        global Config4Lan
        #self.parent.viewGP = self.parent.alert_group
        _gri = int(self.parent.alert_group /2)
        #print(self.parent.GroupSet)
        #單 {0: {'ch': [1], 'durat': (10.69, 10.69, 15.56), 'count': (24, 9, 9), 'sensor': [2, 4], 'triv': ['193.0', ''], 'info': {}}, 1: {'ch': [2], 'durat': [], 'count': [], 'sensor': [], 'triv': ['', ''], 'info': {}}}
        #雙 {0: {'ch': [1, 2], 'durat': (20.39, 20.39, 23.71), 'count': (36, 12, 12), 'sensor': [2, 4], 'triv': ['193.0', ''], 'info': {}}}
        #print(self.parent.alert_group, self.parent.alert_ch)   #單通0, 0，雙通 0 1 ......

        for i in range(0, len(self.parent.GroupSet[self.parent.alert_group]['ch'])):
            _ch = self.parent.GroupSet[self.parent.alert_group]['ch'][i]
            _grj = int(not (_ch %2))
            lbltext = ('%s %s' %(Config4Lan.get(AlarmCfg['lang'], 'channel'), _ch))

            _triv = self.parent.GroupSet[(self.parent.alert_group)]['triv'][_grj]
            #_triv = self.parent.GroupSet[(self.parent.viewGP)]['triv'][i]

            _dt = self.parent.GroupSet[(self.parent.alert_group)]['durat'][_grj]
            #_dt = self.parent.GroupSet[(self.parent.viewGP)]['durat'][i]
            if _dt > 0:
                _dt = ('%.2f' %self.parent.GroupSet[(self.parent.alert_group)]['durat'][_grj])
                #_dt = ('%.2f' %self.parent.GroupSet[(self.parent.viewGP)]['durat'][i])
            else:
                _dt = ''
                
            #print("self.parent.GroupSet[(self.parent.viewGP)]['count'][i]:", self.parent.GroupSet[(self.parent.viewGP)]['count'][i])
            _cs = self.parent.GroupSet[(self.parent.alert_group)]['count'][_grj]
            #_cs = self.parent.GroupSet[(self.parent.viewGP)]['count'][i]
            if _cs > 0:
                _cs = ('%d' %self.parent.GroupSet[self.parent.alert_group]['count'][_grj])
                #_cs = ('%d' %self.parent.GroupSet[(self.parent.viewGP)]['count'][i])
            else:
                _cs = ''
            
            #info_txt = self.parent.GroupSet[(self.parent.viewGP)]['info'][(self.parent.GroupSet[self.parent.viewGP]['ch'][i])]
            #info_txt = textwrap.fill(textwrap.dedent(info_txt.rstrip()), width = 30, max_lines = 2)
            #_c = reduce(lambda x, y: x +y, [int(item[1]) for item in self.parent.GroupSet[self.parent.viewGP]['col'][(i +1)]])
            #if _c >0:
                #_cs = str(_c)
            #else:
                #_cs = ''

            try:
                self.chinfo4hist[i]['senImg'].remove()
            except Exception as e:
                pass

            try:
                sensor = int(self.parent.GroupSet[self.parent.alert_group]['sensor'][_grj])
                #sensor = int(self.parent.GroupSet[(self.parent.viewGP)]['sensor'][i])
                fn = get_sample_data((curPath + "//" + sensors[sensorOption[sensor]][1]),
                                     asfileobj = False)
                arr_img = plt.imread(fn, format = 'png')
                imagebox = OffsetImage(arr_img, zoom = 0.60)
                imagebox.image.axes = self.InfoAx
                self.chinfo4hist[i]['senImg'] = AnnotationBbox(imagebox, [((i *0.34) +0.33), 0.525],
                                                               bboxprops =dict(facecolor = 'none',
                                                                               edgecolor = 'none'))
                self.InfoAx.add_artist(self.chinfo4hist[i]['senImg'])
            except Exception as e:
                pass


            self.ax4main.legend().get_texts()[i].set_text(lbltext)
            
            self.chinfo4hist[i]['chlbl'].set_text(lbltext)

            self.chinfo4hist[i]['triv_txt'].set_text(_triv)

            self.chinfo4hist[i]['count_txt'].set_text(_cs)

            self.chinfo4hist[i]['durat_txt'].set_text(_dt)

            if _grj == self.parent.alert_ch:
                self.chinfo4hist[i]['Frame'].set_color(vars(self.pdstatus_txt)['_color'])
                self.chinfo4hist[i]['Frame'].set_linewidth(2.0)
    '''
    '''
    def drawchart(self):
        global AlarmCfg,GroupSet,figDpi#,colposshift,Ch_Status

        self.def_til_font.set_size(math.ceil(20*72/self.fig4main.dpi))
        #'ax4main_til = OGHHLDCGOGGGBGAFLHGGDG'
        self.ax4main.set_title(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGAFLHGGDG'),
                               fontproperties = self.def_til_font, loc='left')
        self.ax4twmap.set_title(Config4Lan.get(AlarmCfg['lang'], 'TF map'),
                                fontproperties = self.def_til_font, loc='left')
        
        self.def_til_font.set_size(math.ceil(16*72/self.fig4main.dpi))
        self.ax4main.set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGHFDGNGDG'),
                                fontproperties = self.def_til_font)
        self.ax4main.set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'OGHHLDCGOGGGBGGFDGNGDG'),
                                fontproperties = self.def_til_font)
        self.ax4twmap.set_xlabel(Config4Lan.get(AlarmCfg['lang'], 'Equivalent Frequence'),
                                 fontproperties = self.def_til_font)
        self.ax4twmap.set_ylabel(Config4Lan.get(AlarmCfg['lang'], 'Equivalent Timelength'),
                                 fontproperties = self.def_til_font)

        for j in range(0, len(self.parent.GroupSet[self.parent.alert_group]['ch'])):
            self.prpd4main[j][0].set_data(self.parent.Data['data4main'][j]['x'], self.parent.Data['data4main'][j]['y'])
            self.twmap4main[j][0].set_data(self.parent.Data['data4twmp'][j]['x'], self.parent.Data['data4twmp'][j]['y'])
            
            if len(self.parent.Data['data4main'][j]['y']) >0:   #一通道為空(未觸發)時出錯
                maxA = math.ceil(max([abs(self.parent.Data['data4main'][j]['y'][_i]) for _i in range(0, len(self.parent.Data['data4main'][j]['y']))]))
            else:
                maxA = 0
                
            if maxA >= max(self.amp):
                self.amp = [math.sin(math.radians(_a)) *maxA for _a in self.ang]
                self.path4phas.set_data(self.ang, self.amp)
        
        self.ax4main.set_autoscaley_on(True)
        self.ax4twmap.set_autoscaley_on(True)
        self.ax4main.set_xlim([0, 360])
        self.ax4main.set_xticks(list(range(0, 361, 30)))

        self.ax4main.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
        self.def_til_font.set_size(math.ceil(14*72/figDpi))
        [label.set_fontproperties(self.def_til_font) for label in self.ax4main.get_xticklabels()]
        [label.set_fontproperties(self.def_til_font) for label in self.ax4main.get_yticklabels()]

        self.ax4main.relim()
        self.ax4main.autoscale_view()
        self.ax4twmap.relim()
        self.ax4twmap.autoscale_view()
        self.fig4main.canvas.draw()
        self.fig4main.canvas.flush_events()
    '''
#=======================================================================
#======================= InfoScreen Form =========================
class InfoScreen(tk.Toplevel):
    def __init__(self, parent, gr, law, gri):
        tk.Toplevel.__init__(self, parent)
        
        global curPath,VisualNumPad,root,GroupSet,prpd4main,AlarmCfg
        global gainDict,gainCali
        self.gr = gr
        self.gri = gri
        self.law = law
        self.icon = tk.PhotoImage( file = (curPath +'//wave-sine-icon.png'))
        self.title("InfoScreen GR%s" %self.gri)
        self.tk.call('wm', 'iconphoto', self._w, self.icon)
        self.configure(background='#ffffff', takefocus = True, bd = 5)    #背景顏色
        #================== 視窗大小及置中 =================
        wnWidth = self.winfo_screenwidth()
        wnHeight = self.winfo_screenheight()

        w ,h = 520, 130
        size = (w ,h)
        left = (wnWidth - w) /2
        top = (wnHeight - h) /2
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))

        #===================================================
        self.resizable(width = False, height = False)    #可否變更大小
        self.attributes("-topmost", 1)  #最上層顯示
        self.lift()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)    #重新導向 Close Even
        self.transient(parent)
        #self.overrideredirect(True) 
        self.bind("<Unmap>", self.on_exit2)
        #self.bind('<FocusOut>', self.on_exit)

        self.name = None
        self.strUnmap = []
        self.tmpUnmap = None
        self.numUnmap = 0
        self._job =None
        self.ObjID = 'InfoScreen'

        '''
        self.gainA = []
        gainDict = GetGlobals('gainDict')
        gainCali = GetGlobals('gainCali')
        self.gainary = [('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][:4],
                        ('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][-4:]]

        self.valcmd = (self.register(self.gotfocus),
                       '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        '''
        self.infoFrame = tk.Frame(self, bg = '#ffffff')

        for i in range(1, len(GroupSet[self.gr]['ch']) +1):
            _ch = GroupSet[self.gr]['ch'][i -1]
            _chFrm = tk.LabelFrame(self.infoFrame,
                                   relief = tk.GROOVE,
                                    bd = 1,
                                   text = 'CH %s( =SA%s ch %s)' %(_ch, self.gr, (i -1)),
                                   fg = prpd4main[i][0].get_color(),
                                   bg = self['bg'],
                                   font = ('IPAGothic', 12, 'bold'),
                                   height = 40)#,
                                   #width = w)
            _maxlbl = tk.Label(_chFrm, text='Max(Amp.)', relief = tk.FLAT, bd = 0,
                               bg = self['bg'],
                               font = ('IPAGothic', 12, 'bold'), compound ="left")
            _maxlbl.grid(row =0, column =0)
            vars(self)['maxA%s' %(i -1)] =tk.DoubleVar()
            _maxEnt = tk.Entry(_chFrm, relief = tk.GROOVE, bd = 2,
                               textvariable = vars(self)['maxA%s' %(i -1)],
                               bg = self['bg'], 
                               font = ('IPAGothic', 12, 'bold'), width = 8,
                               disabledbackground =self['bg'],
                               disabledforeground = '#0000ff',
                               state = tk.DISABLED)
            _maxEnt.grid(row =0, column =1)
            _maxAlbl = tk.Label(_chFrm, text='mV.', relief = tk.FLAT, bd = 0,
                                bg = self['bg'],
                                font = ('IPAGothic', 12, 'bold'), compound ="left")
            _maxAlbl.grid(row =0, column =2)

            _maxlbl = tk.Label(_chFrm, text='Max(Freq.)', relief = tk.FLAT, bd = 0,
                               bg = self['bg'],
                               font = ('IPAGothic', 12, 'bold'), compound ="left")
            _maxlbl.grid(row =0, column =3)
            vars(self)['maxF%s' %(i -1)] =tk.DoubleVar()
            _maxEnt = tk.Entry(_chFrm, relief = tk.GROOVE, bd = 2,
                               textvariable = vars(self)['maxF%s' %(i -1)],
                               bg = self['bg'], 
                               font = ('IPAGothic', 12, 'bold'), width = 8,
                               disabledbackground =self['bg'],
                               disabledforeground = '#0000ff',
                               state = tk.DISABLED)
            _maxEnt.grid(row =0, column =4)
            _maxAlbl = tk.Label(_chFrm, text='MHz.', relief = tk.FLAT, bd = 0,
                                bg = self['bg'],
                                font = ('IPAGothic', 12, 'bold'), compound ="left")
            _maxAlbl.grid(row =0, column =5)

            _chFrm.pack(anchor =tk.SW, fill =tk.X)

        #============== Get Calibration Parameters =====================
        '''
        self.CaliSet = tk.LabelFrame(self.infoFrame,
                                     relief = tk.GROOVE, bg = self['bg'],
                                     text = 'Config_g%s.ini' %self.gr,
                                     font = ('IPAGothic', 12, 'bold'),
                                     fg = "#0000ff", height = 200,
                                     #width = w,
                                     bd = 1)
        
        self.creatNewCali = False
        self.Config4opt = ConfigLib.ConfigParser()
        self.Config4opt.optionxform = str

        if os.path.isfile((curPath + ('//config_g%s' %self.gr) +'.ini')):
            try:
                self.Config4opt.read((curPath + ('//config_g%s' %self.gr) +'.ini'))
                for j in [0, 1]:
                    try:
                        _k = [key for key in gainDict if gainDict[key][j] == self.gainary[j]][0]
                    except:
                        _k = '10x'
                    _k = _k.strip()
                    self.gainA.append(_k)
                    try:
                        self.coef = self.Config4opt.getfloat('Calibration%s' %j, 'coef_%s' %_k)
                        self.intercept = self.Config4opt.getfloat('Calibration%s' %j, 'intercept_%s' %_k)
                    except:
                        self.creatNewCali = True
            except:
                self.creatNewCali = True
        else:
            self.creatNewCali = True
            
        if self.creatNewCali:
            self.Config4opt = ConfigLib.ConfigParser()
            self.Config4opt.optionxform = str
            for j in [0, 1]:
                self.Config4opt.add_section('Calibration%s' %j)
                for key in gainDict.keys():
                    _k = key.strip()
                    self.Config4opt.set('Calibration%s' %j, 'coef_%s' %_k, str(gainCali[_k][0]))
                    self.Config4opt.set('Calibration%s' %j, 'intercept_%s' %_k, str(gainCali[_k][1]))

        self.calitxtvar = {}
        self.caliEntry = {}
        for i in range(0, len(list(self.Config4opt.sections()))):
            _sec = list(self.Config4opt.sections())[i]
            _lblfrm = tk.LabelFrame(self.CaliSet, relief = tk.GROOVE,
                                    bg = self['bg'],
                                    fg = prpd4main[i +1][0].get_color(),#"#00ff00",
                                    text = '[%s]' %_sec,
                                    font = ('IPAGothic', 12, 'bold')
                                    )
            _lblfrm.grid(column = 0, row =i, stick = tk.SW)
            _opAry = [_op for _op in list(self.Config4opt.options(_sec)) if self.gainA[i] in _op.split('_')]
            _grid_j = 0
            
            for j in range(0, len(list(self.Config4opt.options(_sec)))):
                _opt = list(self.Config4opt.options(_sec))[j]

                self.calitxtvar[len(self.calitxtvar)] = tk.DoubleVar()
                self.caliEntry[len(self.caliEntry)] = adDoubleEntry(_lblfrm)
                self.caliEntry[(len(self.caliEntry) -1)].script = 'Input _g%s/%s' %(self.gr, _opt)
                self.caliEntry[(len(self.caliEntry) -1)].config(textvariable = self.calitxtvar[(len(self.calitxtvar) -1)])
                self.caliEntry[(len(self.caliEntry) -1)].config(bd = 2, font = ('IPAGothic', 12, 'bold'), width = 6)
                self.caliEntry[(len(self.caliEntry) -1)].config(validate = 'focus', validatecommand = self.valcmd)
                self.caliEntry[(len(self.caliEntry) -1)].txtvar =  self.calitxtvar[(len(self.calitxtvar) -1)]
                self.calitxtvar[(len(self.calitxtvar) -1)].set(self.Config4opt.getfloat(_sec, _opt))

                if _opt[:4] == 'coef':
                    tk.Label(_lblfrm, bg = self['bg'],
                             text = _opt,
                             font = ('IPAGothic', 10, 'bold'),
                             relief = tk.FLAT,
                             compound = "left").grid(row = 0, column =(2 *_grid_j), stick = tk.SE)

                    self.caliEntry[(len(self.caliEntry) -1)].grid(row = 0, column =(2 * _grid_j) +1, stick = tk.NE)
                else:
                    tk.Label(_lblfrm, bg = self['bg'],
                             text = _opt,
                             font = ('IPAGothic', 10, 'bold'),
                             relief = tk.FLAT,
                             compound = "left").grid(row = 1, column =(2 *_grid_j), stick = tk.SE)

                    self.caliEntry[(len(self.caliEntry) -1)].grid(row = 1, column =(2 *_grid_j) +1, stick = tk.NE)
                    _grid_j = _grid_j +1
                    
        self.Save4CaliBtn = tk.Button(self.CaliSet, text='Save Calibra', font = ('IPAGothic', 12, 'bold'), image = '',
                                      compound="center", command = self.Save4Cali)
        self.Save4CaliBtn.config(activebackground = "#dddddd", bg = '#ff0000', relief = tk.RAISED, bd = 2, wraplength = 60)
        self.Save4CaliBtn.grid(column = len(list(self.Config4opt.sections())), row =1, stick = tk.SE)

        if self.law >=2:
            self.CaliSet.pack(anchor =tk.SW, fill =tk.X)
        '''
        #======================================================================
        #============================ VisualFltKeyboard ==============================
        '''
        self.VisualFltKeyboard = tk.LabelFrame(self.infoFrame,
                                               relief = tk.GROOVE, bg = self['bg'],
                                               text = '',
                                               fg = "#0000ff",
                                               bd = 1,
                                               #height = 295,
                                               #width = 175, 
                                               )

        self.VisualFltKeyboard.input_var = tk.StringVar()
        self.input = tk.Entry(self.VisualFltKeyboard, bd = 2, textvariable = self.VisualFltKeyboard.input_var, width = 10,
                              font = ('IPAGothic', 14, 'normal'), state = tk.DISABLED,
                              disabledforeground = '#000000', disabledbackground = '#ffffff')
        
        #self.input.place(x =330, y = 5)

        self.btn_list = ['１', '２', '３','４', '５', '６',
                         '７', '８', '９', '０', '．', "±",
                         'Ｃ', 'Ｅｎｔｅｒ']
        ''''''
        self.btn_list = ['１', '２', '３','４', '５', '６',
                         '７', '８', '９', '０', '．', "±",
                         ({
                             'zh-TW' : lambda : '清除',
                             'en-US' : lambda : 'Ｃ',
                             }.get(AlarmCfg['lang'], lambda : '清除')()),
                         ({
                             'zh-TW' : lambda : '確認',
                             'en-US' : lambda : 'Ｅｎｔｅｒ',
                             }.get(AlarmCfg['lang'], lambda : '確認')())]
        ''''''
        self.NumPad = {}
        nCol = 6 #一列有幾個按鈕
        #obj_w = 40     #按紐寬
        #obj_h = 40     #按鈕高
        i = 0

        for i in range(0, len(self.btn_list)):
            #s = i+1
            #row = math.ceil(s / nCol)
            #col = math.ceil(s % nCol)
            #if col == 0:
                #col = nCol
            #row = (row-1) *(obj_h +5)   
            #col = (col-1) *(obj_w +13)
            self.NumPad[i] = VisualKeyboardBtn(self.VisualFltKeyboard, self.btn_list[i])
            if (self.btn_list[i] == '清除' or self.btn_list[i] == 'Ｃ'):
                self.NumPad[i].config(bg = '#ff0000')
                #self.NumPad[i].place(x = 5 + col, y = 5 + row)
                self.NumPad[i].grid(row =0, column = nCol +1, padx = 3, pady = 3, stick = tk.SE)
                pass
            elif (self.btn_list[i] == '確認' or self.btn_list[i] == 'Ｅｎｔｅｒ'):
                self.NumPad[i].config(bg = '#00ff00', width = 11)
                #self.NumPad[i].place(x = 330, y = 50)
                self.NumPad[i].grid(row = int(i /nCol) -1, column = nCol, columnspan = 2, padx = 3, pady = 3, stick = tk.SE)
                pass
            else:
                #self.NumPad[i].place(x = 5 + col, y = 5 + row)
                self.NumPad[i].grid(row = int(i /nCol), column = (i %nCol), padx = 3, pady = 3)

        self.input.grid(row = 0, column = nCol, padx = 3, pady = 3, stick = tk.SE)
        
        #'VisualKeyboardBtnErr_til : JFGGMHKHOGDGEEKGGHNGAGOGNHLGNELHBGKENHNHAFLHGGDG'
        #'VisualKeyboardBtnErr_txt : JFGGMHKHOGDGEEKGGHNGAGOGNHLGNELHBGKENHNHAFLHHHLH'
        til, txt = (Config4Lan.get(AlarmCfg['lang'], 'JFGGMHKHOGDGEEKGGHNGAGOGNHLGNELHBGKENHNHAFLHGGDG'),
                    Config4Lan.get(AlarmCfg['lang'], 'JFGGMHKHOGDGEEKGGHNGAGOGNHLGNELHBGKENHNHAFLHHHLH'))
        ''''''
        til, txt = (
            {
                'zh-TW' : lambda : ("訊息", "注意！輸入格式有誤"),
                'en-US' : lambda : ("Information", "Note！ input format is incorrect"),
                }.get(AlarmCfg['lang'], lambda : ("訊息", "注意！輸入格式有誤"))())
        ''''''
        self.VisualFltKeyboard.errlbl = tk.Label(self.VisualFltKeyboard, text=txt, relief = tk.FLAT, bd = 0,
                                                 bg = self['bg'], fg ='#ff0000',
                                                 font = ('IPAGothic', 14, 'bold'), compound ="left")
        if self.law >=2:
            self.VisualFltKeyboard.pack(anchor =tk.SW, fill =tk.BOTH)
        '''
        #======================================================================

        #self.infoFrame.place(bordermode = tk.OUTSIDE,
                             #width = 520,
                             #height = 420,
                             #x = 0, y = 0)
        self.infoFrame.pack(anchor =tk.SW, fill =tk.X)
        '''
        self.infoFrame.update()
        #w ,h = self.winfo_reqwidth(), self.winfo_reqheight()
        w = self.infoFrame.winfo_width() +15
        h = self.infoFrame.winfo_height() +15
        size = (w ,h)
        left = (wnWidth - w) /2
        top = (wnHeight - h) /2
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))
        '''
    '''
    def Save4Cali(self):
        global curPath,GroupSet

        idx = 0
        for i in range(0, len(list(self.Config4opt.sections()))):
            _sec = list(self.Config4opt.sections())[i]
            _opAry = [_op for _op in list(self.Config4opt.options(_sec)) if self.gainA[i] in _op.split('_')]
            #for j in range(0, len(_opAry)):
                #_opt = _opAry[j]
            for j in range(0, len(list(self.Config4opt.options(_sec)))):
                _opt = list(self.Config4opt.options(_sec))[j]
                self.Config4opt.set(_sec, _opt, str(self.calitxtvar[idx].get()))
                idx = idx +1

        inif = open((curPath + ('//config_g%s' %self.gr) +'.ini'),"w")
        self.Config4opt.write(inif)
        inif.close()

        GroupSet = GetGlobals('GroupSet')
        for j in [0, 1]:
            for key in gainDict.keys():
                _k = key.strip()    #1x,10x,20x
                GroupSet[self.gr]['Calib'][j]['coef'].update({_k : self.Config4opt.getfloat('Calibration%s' %j, 'coef_%s' %_k)})
                GroupSet[self.gr]['Calib'][j]['intercept'].update({_k : self.Config4opt.getfloat('Calibration%s' %j, 'intercept_%s' %_k)})

        UpdateGlobals('GroupSet', GroupSet)
        GroupSet = GetGlobals('GroupSet')
        pass
        
    def negclick(self):
        try:
            _v = float(self.VisualFltKeyboard.input_var.get())
            self.VisualFltKeyboard.input_var.set(str(_v *(-1)))
        except:
            pass
        pass

    def gotfocus(self, d, i, P, s, S, v, V, W):
        global root
        self.obj = self.nametowidget(W)
        
        if V == 'focusin':
            key = [key for key in self.caliEntry.keys() if self.caliEntry[key] == self.obj][0]
            vars(self.VisualFltKeyboard)['actObj'] = self.calitxtvar[key]
            self.ActInputObj = self.obj
            self.obj.config(background = "#80FF80")
            #self.VisualFltKeyboard.input_var.set(self.obj.get())
            #self.VisualFltKeyboard.pack(anchor =tk.SW, fill =tk.X)
        elif V == 'focusout':
            self.ActInputObj = None
            self.obj.config(background = self.obj.oldfg)
            #self.VisualFltKeyboard.input_var.set('')
            #self.VisualFltKeyboard.pack_forget()

        return True
    '''
    def on_exit(self, *args):
        PopGlobals(self.name)
        self.destroy()
        '''
        try:
            GetGlobals(self.name).destroy()
            PopGlobals(self.name)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            try:
                PopGlobals(self.name)
                self.destroy()
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
        pass
        '''

    def on_exit2(self, *args):
        self.strUnmap.append(time.time())
        if self._job is None:
            self._job = self.after(100, self.update_clock)

    def update_clock(self):
        global root
        root.deiconify()
        root.focus_set()
        if self.tmpUnmap == max(self.strUnmap):
            self.numUnmap = self.numUnmap +1
            if self.numUnmap >=2:
                if self._job is not None:
                    self.after_cancel(self._job)
                    self._job = None
                self.on_exit()
                pass
        else:
            self.tmpUnmap = max(self.strUnmap)
            self.numUnmap = 0

        self._job = self.after(100, self.update_clock)

#========================================
#======================= InfoScreen Form =========================
class InfoScreen2(tk.Toplevel):
    def __init__(self, parent, gr, law, gri):
        tk.Toplevel.__init__(self, parent)
        
        global curPath,VisualNumPad,root,GroupSet,prpd4main,AlarmCfg
        global gainDict,gainCali
        self.gr = gr
        self.gri = gri
        self.law = law
        self.icon = tk.PhotoImage( file = (curPath +'//wave-sine-icon.png'))
        self.title("InfoScreen GR%s" %self.gri)
        self.tk.call('wm', 'iconphoto', self._w, self.icon)
        self.configure(background='#ffffff', takefocus = True, bd = 5)    #背景顏色
        #================== 視窗大小及置中 =================
        wnWidth = self.winfo_screenwidth()
        wnHeight = self.winfo_screenheight()

        w ,h = 620, 400
        size = (w ,h)
        left = (wnWidth - w) /2
        top = (wnHeight - h) /2
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))

        #===================================================
        self.resizable(width = False, height = False)    #可否變更大小
        self.attributes("-topmost", 1)  #最上層顯示
        self.lift()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)    #重新導向 Close Even
        self.transient(parent)
        #self.overrideredirect(True) 
        self.bind("<Unmap>", self.on_exit2)
        #self.bind('<FocusOut>', self.on_exit)

        self.name = None
        self.strUnmap = []
        self.tmpUnmap = None
        self.numUnmap = 0
        self._job =None
        self.ObjID = 'InfoScreen'

        self.gainA = []
        gainDict = GetGlobals('gainDict')
        gainCali = GetGlobals('gainCali')
        self.gainary = [('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][:4],
                        ('00000000' +bin(GroupSet[self.gr]['gain'])[2:])[-8:][-4:]]

        self.valcmd = (self.register(self.gotfocus),
                       '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.infoFrame = tk.Frame(self, bg = '#ffffff')

        for i in range(1, len(GroupSet[self.gr]['ch']) +1):
            _ch = GroupSet[self.gr]['ch'][i -1]
            _chFrm = tk.LabelFrame(self.infoFrame,
                                   relief = tk.GROOVE,
                                    bd = 1,
                                   text = 'CH %s( =SA%s ch %s)' %(_ch, self.gr, (i -1)),
                                   fg = prpd4main[i][0].get_color(),
                                   bg = self['bg'],
                                   font = ('IPAGothic', 12, 'bold'),
                                   height = 40)#,
                                   #width = w)
            _maxlbl = tk.Label(_chFrm, text='Max(Amp.)', relief = tk.FLAT, bd = 0,
                               bg = self['bg'],
                               font = ('IPAGothic', 12, 'bold'), compound ="left")
            _maxlbl.grid(row =0, column =0)
            vars(self)['maxA%s' %(i -1)] =tk.DoubleVar()
            _maxEnt = tk.Entry(_chFrm, relief = tk.GROOVE, bd = 2,
                               textvariable = vars(self)['maxA%s' %(i -1)],
                               bg = self['bg'], 
                               font = ('IPAGothic', 12, 'bold'), width = 8,
                               disabledbackground =self['bg'],
                               disabledforeground = '#0000ff',
                               state = tk.DISABLED)
            _maxEnt.grid(row =0, column =1)
            _maxAlbl = tk.Label(_chFrm, text='mV.', relief = tk.FLAT, bd = 0,
                                bg = self['bg'],
                                font = ('IPAGothic', 12, 'bold'), compound ="left")
            _maxAlbl.grid(row =0, column =2)

            _maxlbl = tk.Label(_chFrm, text='Max(Freq.)', relief = tk.FLAT, bd = 0,
                               bg = self['bg'],
                               font = ('IPAGothic', 12, 'bold'), compound ="left")
            _maxlbl.grid(row =0, column =3)
            vars(self)['maxF%s' %(i -1)] =tk.DoubleVar()
            _maxEnt = tk.Entry(_chFrm, relief = tk.GROOVE, bd = 2,
                               textvariable = vars(self)['maxF%s' %(i -1)],
                               bg = self['bg'], 
                               font = ('IPAGothic', 12, 'bold'), width = 8,
                               disabledbackground =self['bg'],
                               disabledforeground = '#0000ff',
                               state = tk.DISABLED)
            _maxEnt.grid(row =0, column =4)
            _maxAlbl = tk.Label(_chFrm, text='MHz.', relief = tk.FLAT, bd = 0,
                                bg = self['bg'],
                                font = ('IPAGothic', 12, 'bold'), compound ="left")
            _maxAlbl.grid(row =0, column =5)

            _chFrm.pack(anchor =tk.SW, fill =tk.X)

        #============== Get Calibration Parameters =====================

        self.CaliSet = tk.LabelFrame(self.infoFrame,
                                     relief = tk.GROOVE, bg = self['bg'],
                                     text = 'Config_g%s.ini' %self.gr,
                                     font = ('IPAGothic', 12, 'bold'),
                                     fg = "#0000ff", height = 200,
                                     #width = w,
                                     bd = 1)
        
        self.creatNewCali = False
        self.Config4opt = ConfigLib.ConfigParser()
        self.Config4opt.optionxform = str

        if os.path.isfile((curPath + ('//config_g%s' %self.gr) +'.ini')):
            try:
                self.Config4opt.read((curPath + ('//config_g%s' %self.gr) +'.ini'))
                for j in [0, 1]:
                    try:
                        _k = [key for key in gainDict if gainDict[key][j] == self.gainary[j]][0]
                    except:
                        _k = '10x'
                    _k = _k.strip()
                    self.gainA.append(_k)
                    try:
                        self.coef = self.Config4opt.getfloat('Calibration%s' %j, 'coef_%s' %_k)
                        self.intercept = self.Config4opt.getfloat('Calibration%s' %j, 'intercept_%s' %_k)
                    except:
                        self.creatNewCali = True
            except:
                self.creatNewCali = True
        else:
            self.creatNewCali = True
            
        if self.creatNewCali:
            self.Config4opt = ConfigLib.ConfigParser()
            self.Config4opt.optionxform = str
            for j in [0, 1]:
                self.Config4opt.add_section('Calibration%s' %j)
                for key in gainDict.keys():
                    _k = key.strip()
                    self.Config4opt.set('Calibration%s' %j, 'coef_%s' %_k, str(gainCali[_k][0]))
                    self.Config4opt.set('Calibration%s' %j, 'intercept_%s' %_k, str(gainCali[_k][1]))

        self.calitxtvar = {}
        self.caliEntry = {}
        for i in range(0, len(list(self.Config4opt.sections()))):
            _sec = list(self.Config4opt.sections())[i]
            _lblfrm = tk.LabelFrame(self.CaliSet, relief = tk.GROOVE,
                                    bg = self['bg'],
                                    fg = prpd4main[i +1][0].get_color(),#"#00ff00",
                                    text = '[%s]' %_sec,
                                    font = ('IPAGothic', 12, 'bold')
                                    )
            _lblfrm.grid(column = 0, row =i, stick = tk.SW)
            _opAry = [_op for _op in list(self.Config4opt.options(_sec)) if self.gainA[i] in _op.split('_')]
            _grid_j = 0
            
            for j in range(0, len(list(self.Config4opt.options(_sec)))):
                _opt = list(self.Config4opt.options(_sec))[j]

                self.calitxtvar[len(self.calitxtvar)] = tk.DoubleVar()
                self.caliEntry[len(self.caliEntry)] = adDoubleEntry(_lblfrm)
                self.caliEntry[(len(self.caliEntry) -1)].script = 'Input _g%s/%s' %(self.gr, _opt)
                self.caliEntry[(len(self.caliEntry) -1)].config(textvariable = self.calitxtvar[(len(self.calitxtvar) -1)])
                self.caliEntry[(len(self.caliEntry) -1)].config(bd = 2, font = ('IPAGothic', 12, 'bold'), width = 6)
                self.caliEntry[(len(self.caliEntry) -1)].config(validate = 'focus', validatecommand = self.valcmd)
                self.caliEntry[(len(self.caliEntry) -1)].txtvar =  self.calitxtvar[(len(self.calitxtvar) -1)]
                self.calitxtvar[(len(self.calitxtvar) -1)].set(self.Config4opt.getfloat(_sec, _opt))

                if _opt[:4] == 'coef':
                    tk.Label(_lblfrm, bg = self['bg'],
                             text = _opt,
                             font = ('IPAGothic', 10, 'bold'),
                             relief = tk.FLAT,
                             compound = "left").grid(row = 0, column =(2 *_grid_j), stick = tk.SE)

                    self.caliEntry[(len(self.caliEntry) -1)].grid(row = 0, column =(2 * _grid_j) +1, stick = tk.NE)
                else:
                    tk.Label(_lblfrm, bg = self['bg'],
                             text = _opt,
                             font = ('IPAGothic', 10, 'bold'),
                             relief = tk.FLAT,
                             compound = "left").grid(row = 1, column =(2 *_grid_j), stick = tk.SE)

                    self.caliEntry[(len(self.caliEntry) -1)].grid(row = 1, column =(2 *_grid_j) +1, stick = tk.NE)
                    _grid_j = _grid_j +1
                    
        self.Save4CaliBtn = tk.Button(self.CaliSet, text='Save Calibra', font = ('IPAGothic', 12, 'bold'), image = '',
                                      compound="center", command = self.Save4Cali)
        self.Save4CaliBtn.config(activebackground = "#dddddd", bg = '#ff0000', relief = tk.RAISED, bd = 2, wraplength = 60)
        self.Save4CaliBtn.grid(column = len(list(self.Config4opt.sections())), row =1, stick = tk.SE)

        self.CaliSet.pack(anchor =tk.SW, fill =tk.X)

        #======================================================================
        #============================ VisualFltKeyboard ==============================
        self.VisualFltKeyboard = tk.LabelFrame(self.infoFrame,
                                               relief = tk.GROOVE, bg = self['bg'],
                                               text = '',
                                               fg = "#0000ff",
                                               bd = 1,
                                               #height = 295,
                                               #width = 175, 
                                               )

        self.VisualFltKeyboard.input_var = tk.StringVar()
        self.input = tk.Entry(self.VisualFltKeyboard, bd = 2, textvariable = self.VisualFltKeyboard.input_var, width = 10,
                              font = ('IPAGothic', 14, 'normal'), state = tk.DISABLED,
                              disabledforeground = '#000000', disabledbackground = '#ffffff')
        
        #self.input.place(x =330, y = 5)

        self.btn_list = ['１', '２', '３','４', '５', '６',
                         '７', '８', '９', '０', '．', "±",
                         'Ｃ', 'Ｅｎｔｅｒ']
        '''
        self.btn_list = ['１', '２', '３','４', '５', '６',
                         '７', '８', '９', '０', '．', "±",
                         ({
                             'zh-TW' : lambda : '清除',
                             'en-US' : lambda : 'Ｃ',
                             }.get(AlarmCfg['lang'], lambda : '清除')()),
                         ({
                             'zh-TW' : lambda : '確認',
                             'en-US' : lambda : 'Ｅｎｔｅｒ',
                             }.get(AlarmCfg['lang'], lambda : '確認')())]
        '''
        self.NumPad = {}
        nCol = 6 #一列有幾個按鈕
        #obj_w = 40     #按紐寬
        #obj_h = 40     #按鈕高
        i = 0

        for i in range(0, len(self.btn_list)):
            #s = i+1
            #row = math.ceil(s / nCol)
            #col = math.ceil(s % nCol)
            #if col == 0:
                #col = nCol
            #row = (row-1) *(obj_h +5)   
            #col = (col-1) *(obj_w +13)
            self.NumPad[i] = VisualKeyboardBtn(self.VisualFltKeyboard, self.btn_list[i])
            if (self.btn_list[i] == '清除' or self.btn_list[i] == 'Ｃ'):
                self.NumPad[i].config(bg = '#ff0000')
                #self.NumPad[i].place(x = 5 + col, y = 5 + row)
                self.NumPad[i].grid(row =0, column = nCol +1, padx = 3, pady = 3, stick = tk.SE)
                pass
            elif (self.btn_list[i] == '確認' or self.btn_list[i] == 'Ｅｎｔｅｒ'):
                self.NumPad[i].config(bg = '#00ff00', width = 11)
                #self.NumPad[i].place(x = 330, y = 50)
                self.NumPad[i].grid(row = int(i /nCol) -1, column = nCol, columnspan = 2, padx = 3, pady = 3, stick = tk.SE)
                pass
            else:
                #self.NumPad[i].place(x = 5 + col, y = 5 + row)
                self.NumPad[i].grid(row = int(i /nCol), column = (i %nCol), padx = 3, pady = 3)

        self.input.grid(row = 0, column = nCol, padx = 3, pady = 3, stick = tk.SE)
        
        #'VisualKeyboardBtnErr_til : JFGGMHKHOGDGEEKGGHNGAGOGNHLGNELHBGKENHNHAFLHGGDG'
        #'VisualKeyboardBtnErr_txt : JFGGMHKHOGDGEEKGGHNGAGOGNHLGNELHBGKENHNHAFLHHHLH'
        til, txt = (Config4Lan.get(AlarmCfg['lang'], 'JFGGMHKHOGDGEEKGGHNGAGOGNHLGNELHBGKENHNHAFLHGGDG'),
                    Config4Lan.get(AlarmCfg['lang'], 'JFGGMHKHOGDGEEKGGHNGAGOGNHLGNELHBGKENHNHAFLHHHLH'))
        '''
        til, txt = (
            {
                'zh-TW' : lambda : ("訊息", "注意！輸入格式有誤"),
                'en-US' : lambda : ("Information", "Note！ input format is incorrect"),
                }.get(AlarmCfg['lang'], lambda : ("訊息", "注意！輸入格式有誤"))())
        '''
        self.VisualFltKeyboard.errlbl = tk.Label(self.VisualFltKeyboard, text=txt, relief = tk.FLAT, bd = 0,
                                                 bg = self['bg'], fg ='#ff0000',
                                                 font = ('IPAGothic', 14, 'bold'), compound ="left")
          
        #======================================================================

        #self.infoFrame.place(bordermode = tk.OUTSIDE,
                             #width = 520,
                             #height = 420,
                             #x = 0, y = 0)
        self.infoFrame.pack(anchor =tk.SW, fill =tk.X)
        '''
        self.infoFrame.update()
        #w ,h = self.winfo_reqwidth(), self.winfo_reqheight()
        w = self.infoFrame.winfo_width() +15
        h = self.infoFrame.winfo_height() +15
        size = (w ,h)
        left = (wnWidth - w) /2
        top = (wnHeight - h) /2
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))
        '''
    def Save4Cali(self):
        global curPath,GroupSet

        idx = 0
        for i in range(0, len(list(self.Config4opt.sections()))):
            _sec = list(self.Config4opt.sections())[i]
            _opAry = [_op for _op in list(self.Config4opt.options(_sec)) if self.gainA[i] in _op.split('_')]
            #for j in range(0, len(_opAry)):
                #_opt = _opAry[j]
            for j in range(0, len(list(self.Config4opt.options(_sec)))):
                _opt = list(self.Config4opt.options(_sec))[j]
                self.Config4opt.set(_sec, _opt, str(self.calitxtvar[idx].get()))
                idx = idx +1

        inif = open((curPath + ('//config_g%s' %self.gr) +'.ini'),"w")
        self.Config4opt.write(inif)
        inif.close()

        GroupSet = GetGlobals('GroupSet')
        for j in [0, 1]:
            for key in gainDict.keys():
                _k = key.strip()    #1x,10x,20x
                GroupSet[self.gr]['Calib'][j]['coef'].update({_k : self.Config4opt.getfloat('Calibration%s' %j, 'coef_%s' %_k)})
                GroupSet[self.gr]['Calib'][j]['intercept'].update({_k : self.Config4opt.getfloat('Calibration%s' %j, 'intercept_%s' %_k)})

        UpdateGlobals('GroupSet', GroupSet)
        GroupSet = GetGlobals('GroupSet')
        pass
        
    def negclick(self):
        try:
            _v = float(self.VisualFltKeyboard.input_var.get())
            self.VisualFltKeyboard.input_var.set(str(_v *(-1)))
        except:
            pass
        pass

    def gotfocus(self, d, i, P, s, S, v, V, W):
        global root
        self.obj = self.nametowidget(W)
        
        if V == 'focusin':
            key = [key for key in self.caliEntry.keys() if self.caliEntry[key] == self.obj][0]
            vars(self.VisualFltKeyboard)['actObj'] = self.calitxtvar[key]
            self.ActInputObj = self.obj
            #self.VisualFltKeyboard.input_var.set(self.obj.get())
            #self.VisualFltKeyboard.pack(anchor =tk.SW, fill =tk.X)
        elif V == 'focusout':
            self.ActInputObj = None
            self.obj.config(background = self.obj.oldfg)
            #self.VisualFltKeyboard.input_var.set('')
            #self.VisualFltKeyboard.pack_forget()

        return True

    def on_exit(self, *args):
        PopGlobals(self.name)
        self.destroy()
        '''
        try:
            GetGlobals(self.name).destroy()
            PopGlobals(self.name)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            try:
                PopGlobals(self.name)
                self.destroy()
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
        pass
        '''

    def on_exit2(self, *args):
        self.strUnmap.append(time.time())
        if self._job is None:
            self._job = self.after(100, self.update_clock)

    def update_clock(self):
        global root
        root.deiconify()
        root.focus_set()
        if self.tmpUnmap == max(self.strUnmap):
            self.numUnmap = self.numUnmap +1
            if self.numUnmap >=2:
                if self._job is not None:
                    self.after_cancel(self._job)
                    self._job = None
                self.on_exit()
                pass
        else:
            self.tmpUnmap = max(self.strUnmap)
            self.numUnmap = 0

        self._job = self.after(100, self.update_clock)

#========================================
#========= class getpinstat=====================
'''
class getpinstat(threading.Thread):
    def __init__(self, threadID, name, obj, delay, t0, freq, pin):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.obj = obj
        self.delay = delay
        self.t0 = t0
        self.freq = freq
        self.ts = []
        self.dt = delay
        self.pin = pin
        self.isPASS = False
        self.isGPIO = None
        self.period = None
        
    def run(self):
        global threadLock,curPath,GPIO,thisOS
        curPath = GetGlobals('curPath')
        GPIO = GetGlobals('GPIO')
        thisOS = GetGlobals('thisOS')
        ''''''
        threadLock = threading.Lock()
        threadLock.acquire()
        # 釋放鎖
        if threadLock == "locked":
            threadLock.release()
        ''''''
        self.dt = self.delay

        try:
            GPIO
            self.isGPIO = True
        except:
            self.isGPIO = False
            pass
        if self.isGPIO:
            try:
                GPIO.remove_event_detect(self.pin)
            except:
                pass
            
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin, GPIO.IN)

            self.period = 1/self.freq

            commLine = ('sudo python3 ' + curPath + '//PWMTrig.py ' +
                        str(self.pin) + ' ' + (curPath + "//pwm.~ ") + str(self.freq))

            p4get = subprocess.Popen(commLine,
                                     stderr = subprocess.STDOUT,
                                     stdout = subprocess.PIPE,
                                     shell = True,
                                     preexec_fn = os.setsid if thisOS == 'Linux' else None)

            #p4get = subprocess.Popen(commLine, stdout=subprocess.PIPE,
                                     #shell=True, preexec_fn=os.setsid)

            time.sleep(1)   #必要的延遲
            
            commLine = ('sudo python3 ' + curPath + '//PINPWM.py '+
                        str(self.pin) + ' '+ str(self.freq))


            p4pwm = subprocess.Popen(commLine,
                                     stderr = subprocess.STDOUT,
                                     stdout = subprocess.PIPE,
                                     shell = True,
                                     preexec_fn = os.setsid if thisOS == 'Linux' else None)
            
            #p4pwm = subprocess.Popen(commLine, stdout=subprocess.PIPE,
                                     #shell=True, preexec_fn=os.setsid)

            time.sleep(1)

            while self.dt >= 0:
                self.dt = int(self.delay -(time.time() -self.t0))

            try:
                p4pwm
                while True:
                    if p4pwm.poll() is not None:
                        break
                    os.killpg(os.getpgid(p4pwm.pid), signal.SIGTERM)
                ''''''
                os.killpg(os.getpgid(p4pwm.pid), signal.SIGTERM)
                while p4pwm.poll() is None:
                    pass
                ''''''
            except:
                pass
            
            try:
                p4get
                while True:
                    if p4get.poll() is not None:
                        break
                    os.killpg(os.getpgid(p4get.pid), signal.SIGTERM)
                ''''''
                os.killpg(os.getpgid(p4get.pid), signal.SIGTERM)
                while p4get.poll() is None:
                    pass
                ''''''
            except:
                pass
            
            GPIO.cleanup()

            if os.path.isfile((curPath + "//pwm.~")):
                pwmf = open((curPath + "//pwm.~"), "r")
                self.ts = np.array(list(csv.reader(pwmf))).astype(float)
                pwmf.close()

            if len(self.ts) >0:
                f = (len(self.ts) -1)/(self.ts[-1][0] -self.ts[0][0])
                print('f:', int(round(f, 0)), 'self.freq:', self.freq) 
                if int(round(f, 0)) == self.freq:
                    self.isPASS = 'T'
                else:
                    self.isPASS = 'F'
            else:
                self.isPASS = 'F'

            os.remove((curPath + '//pwm.~'))

        else:
            while self.dt >= 0:
                self.dt = int(self.delay -(time.time() -self.t0))

            self.isPASS = 'E'
'''
#====================================================================
#===================== serialerrform ===============================
class serialerrform(tk.Toplevel):
    def __init__(self, parent, til, txt):
        tk.Toplevel.__init__(self, parent)
        global Opt2ActFrm,root,curPath,AlarmCfg,tilBar,StatusBar,ChxStatus,Config4Lan,root
        self.title(til)
        self.attributes("-topmost", 1) #最上層顯示
        self.configure(background='#eeeeee', takefocus = True, relief = tk.RAISED, bd = 2)    #背景顏色
        #================== 視窗大小及置中 =================
        wnWidth = self.winfo_screenwidth()
        wnHeight = self.winfo_screenheight()
        '''
        w ,h = 340, 150
        size = (w ,h)
        left = (wnWidth - w) /2
        top = (wnHeight - h) /2
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))
        '''
        #===================================================
        self.protocol("WM_DELETE_WINDOW", self.on_exit)    #重新導向 Close Even
        #self.transient(parent)
        self.overrideredirect(True)

        root = GetGlobals('root')
        Config4Lan = GetGlobals('Config4Lan')
        AlarmCfg = GetGlobals('AlarmCfg')
        '''
        ChxStatus = GetGlobals('ChxStatus')
        UpdateOptStates(tilBar, 0)
        UpdateOptStates(StatusBar, 0)
        UpdateOptStates(ChxStatus, 0)
        self.thisFrm = tilBar.control_variable.get()
        self.lKey = [key for key, value in Opt2ActFrm.items() if value == ([x for x in Opt2ActFrm.values() if self.thisFrm in x][0])][0]
        UpdateOptStates(Opt2ActFrm[self.lKey][2], 0)
        '''
        
        self.name = None
        self.strUnmap = []
        self.tmpUnmap = time.time()
        self.numUnmap = 0
        self._job =None
        self.limit = 30

        self.BackFrm = tk.Frame(self, relief = tk.FLAT, bg = self['bg'],
                                #width = w, height = h,
                                bd = 0)

        self.icon4til = Image.open((curPath + "//Alert.png"))
        self.icon4til = self.icon4til.resize((45, 45), Image.ANTIALIAS)
        self.icon4til = ImageTk.PhotoImage(self.icon4til)
        self.msg_var = tk.StringVar()
        self.msg_var.set(txt)
        self.msgtxt = tk.Label(self.BackFrm,
                               textvariable = self.msg_var,
                               relief = tk.FLAT, bd = 0,
                               font = ('IPAGothic', 24, 'normal'),
                               compound = "left",
                               image = self.icon4til)

        self.btn_var = tk.StringVar()
        self.btn_var.set('%s timeout：%s' %(Config4Lan.get(AlarmCfg['lang'], 'ok'), self.limit))
        self.chkbtn= tk.Button(self.BackFrm,
                               textvariable = self.btn_var, image = None,
                               compound="center",
                               fg = '#ff0000',
                               font = ('IPAGothic', 24, 'normal'),
                               command = self.on_exit)

        self.msgtxt.pack(side = 'top', fill =tk.X)
        self.chkbtn.pack(side ='bottom', fill =tk.X)
        self.BackFrm.pack()
        self.update()
        size = (self.winfo_reqwidth() ,self.winfo_reqheight())
        left = (wnWidth - size[0]) /2
        top = (wnHeight - size[1]) /2
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))
        self.resizable(width = False, height = False)    #可否變更大小
        self.refreshIdlefun = None
        self.refreshIdlelbl()

    def refreshIdlelbl(self):
        if self.limit >0:
            self.limit = self.limit -1
            self.btn_var.set('%s timeout：%s' %(Config4Lan.get(AlarmCfg['lang'], 'ok'), self.limit))
            self.refreshIdlefun = self.after(1000, self.refreshIdlelbl)
        else:
            if self.refreshIdlefun is not None:
                self.after_cancel(self.refreshIdlefun)
                self.refreshIdlefun = None
            self.on_exit()
            

    def on_exit(self):
        global VisualNumPad,tilBar,StatusBar,ChxStatus,root,SerPortErrform
        AlarmCfg['demo'] = 99
        UpdateGlobals('AlarmCfg', AlarmCfg)
        self.destroy()
        PopGlobals(self.name)
        args = [root]
        SerPortErrform = CreateVisualKeyboard('serialinsertform', 'SerPortErrform', args)
        root.updatemain()
        root.focus_set()
        '''
        UpdateOptStates(tilBar, 1)
        UpdateOptStates(StatusBar, 1)
        UpdateOptStates(ChxStatus, 1)
        UpdateOptStates(Opt2ActFrm[self.lKey][2], 1)
        '''
#========================================================
#===================== usberrform ===============================
class usberrform(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        global root
        root = GetGlobals('root')
        self.icon = tk.PhotoImage( file = (curPath +'//08-512.png'))
        self.title('USB Error')
        self.tk.call('wm', 'iconphoto', self._w, self.icon)
        self.configure(background='#eeeeee', takefocus = True, relief = tk.RAISED, bd = 2)    #背景顏色
        #================== 視窗大小及置中 =================
        wnWidth = self.winfo_screenwidth()
        wnHeight = self.winfo_screenheight()

        #===================================================
        self.resizable(width = False, height = False)    #可否變更大小
        self.attributes("-topmost", 1) #最上層顯示
        self.lift()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)    #重新導向 Close Even
        self.transient(parent)
        #self.overrideredirect(True)
        self.bind("<Unmap>", self.on_exit2)

        self.name = None
        self.strUnmap = []
        self.tmpUnmap = None
        self.numUnmap = 0
        self._job =None
        self.ObjID = 'usberrform'

        self.BackFrm = tk.Frame(self, relief = tk.FLAT, bg = self['bg'],
                                #width = w, height = h,
                                bd = 0)

        self.icon4til = Image.open((curPath + "//usbdiskerror.png"))
        self.icon4til = self.icon4til.resize((100, 100), Image.ANTIALIAS)
        self.icon4til = ImageTk.PhotoImage(self.icon4til)

        self.msg_var = tk.StringVar()
        self.msg_var.set('USB Disk Error!')
        self.msgtxt = tk.Label(self.BackFrm,
                               textvariable = self.msg_var,
                               relief = tk.FLAT, bd = 0,
                               fg = '#ff0000',
                               font = ('IPAGothic', 48, 'normal'),
                               compound = "left",
                               image = self.icon4til)


        self.msgtxt.pack(side = 'top', fill =tk.X)

        self.BackFrm.pack()
        self.update()
        size = (self.winfo_reqwidth() ,self.winfo_reqheight())
        left = (wnWidth - size[0]) /2
        top = (wnHeight - size[1]) /2
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))
        self.resizable(width = False, height = False)    #可否變更大小
        #self.refreshIdlefun = None
        #self.refreshIdlelbl()

    def on_exit(self):
        global root
        pass

    def on_exit2(self, *args):
        self.strUnmap.append(time.time())
        if self._job is None:
            self._job = self.after(100, self.update_clock)

    def update_clock(self):
        global root
        root.deiconify()
        root.focus_set()
        if self.tmpUnmap == max(self.strUnmap):
            self.numUnmap = self.numUnmap +1
            if self.numUnmap >=2:
                if self._job is not None:
                    self.after_cancel(self._job)
                    self._job = None
                self.on_exit()
                pass
        else:
            self.tmpUnmap = max(self.strUnmap)
            self.numUnmap = 0

        self._job = self.after(100, self.update_clock)
#========================================================
#===================== serialinsertform ===============================
class serialinsertform(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        global root
        root = GetGlobals('root')
        self.icon = tk.PhotoImage( file = (curPath +'//08-512.png'))
        self.title('Serial Cable Error')
        self.tk.call('wm', 'iconphoto', self._w, self.icon)
        self.configure(background='#eeeeee', takefocus = True, relief = tk.RAISED, bd = 2)    #背景顏色
        #================== 視窗大小及置中 =================
        wnWidth = self.winfo_screenwidth()
        wnHeight = self.winfo_screenheight()

        #===================================================
        self.resizable(width = False, height = False)    #可否變更大小
        self.attributes("-topmost", 1) #最上層顯示
        self.lift()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)    #重新導向 Close Even
        self.transient(parent)
        #self.overrideredirect(True)
        self.bind("<Unmap>", self.on_exit2)

        self.name = None
        self.strUnmap = []
        self.tmpUnmap = None
        self.numUnmap = 0
        self._job =None
        self.ObjID = 'serialinsertform'

        self.BackFrm = tk.Frame(self, relief = tk.FLAT, bg = self['bg'],
                                #width = w, height = h,
                                bd = 0)

        self.icon4til = Image.open((curPath + "//cableconn.jpg"))
        self.icon4til = self.icon4til.resize((125, 77), Image.ANTIALIAS)
        self.icon4til = ImageTk.PhotoImage(self.icon4til)

        self.msg_var = tk.StringVar()
        self.msg_var.set('')
        self.msgtxt = tk.Label(self.BackFrm,
                               textvariable = self.msg_var,
                               relief = tk.FLAT, bd = 0,
                               fg = '#ff0000',
                               font = ('IPAGothic', 48, 'normal'),
                               compound = "left",
                               image = self.icon4til)


        self.msgtxt.pack(side = 'top', fill =tk.X)

        self.BackFrm.pack()
        self.update()
        size = (self.winfo_reqwidth() ,self.winfo_reqheight())
        left = (wnWidth - size[0])
        top = (wnHeight - size[1]) /2
        self.geometry("%dx%d+%d+%d" % (size + (left, top)))
        self.resizable(width = False, height = False)    #可否變更大小
        #self.refreshIdlefun = None
        #self.refreshIdlelbl()

    def on_exit(self):
        global root
        pass

    def on_exit2(self, *args):
        self.strUnmap.append(time.time())
        if self._job is None:
            self._job = self.after(100, self.update_clock)

    def update_clock(self):
        global root
        root.deiconify()
         if self.tmpUnmap == max(self.strUnmap):
            self.numUnmap = self.numUnmap +1
            if self.numUnmap >=2:
                if self._job is not None:
                    self.after_cancel(self._job)
                    self._job = None
                self.on_exit()
                pass
        else:
            self.tmpUnmap = max(self.strUnmap)
            self.numUnmap = 0

        self._job = self.after(100, self.update_clock)
#========================================================
