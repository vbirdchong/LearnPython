#! python3
# coding=utf-8

import sys

USAGE_INFO = '''
Usage: python PRGroup.py [group_name]
 group_name: TDDMACPS/UEC/CLEEC...
 e.g.: python PRGroup.py UEC'''

TDDMACPS = {
    'group': 'NIHZSMAC',
    'email': 'I_EXT_MBB_GLOBAL_LTE_TDD_RRM_MAINTENANCE_GMS'
}

DLPHY = {
    'group': 'NIHZSPHYDL',
    'email': 'I_EXT_MBB_LTE_TDSW_PHYDL_PR_GMS '
}

ULPHY = {
    'group': 'NIHZSPHYUL',
    'email': 'I_EXT_MBB_LTE_TD_PHY_UL_MAINT_GROUP_GMS_GMS'
}

CELLC = {
    'group': 'RABLTESWCELLC',
    'email': 'I_EXT_LTE_CP_CELLC_FAULT_ANALYSIS'
}

UEC = {
    'group': 'RABLTESWUEC',
    'email': 'I_EXT_LTE_CP_UEC_FAULT_ANALYSIS_GMS_GMS'
}

L2 = {
    'group': 'RABLTESWFOUL2',
    'email': 'I_EXT_MBB_LTE_L2_PRESCREENING_GMS'
}

ALLGROUP = {
    'TDDMACPS':     TDDMACPS,
    'DLPHY':        DLPHY,
    'ULPHY':        ULPHY,
    'CELLC':        CELLC,
    'UEC':          UEC,
    'L2':           L2
}

def printInfo(swList):
    print('PR Group' + '\t\t\t' + 'Email Group')
    for sw in swList:
        info = ALLGROUP[sw]
        print(info['group'] + '\t\t\t' + info['email'])

def main():
    print(sys.argv)

    swList = []
    if (len(sys.argv) == 1):
        # print all groups
        swList = ['TDDMACPS', 'DLPHY', 'ULPHY', 'CELLC', 'UEC', 'L2']
    elif (len(sys.argv) == 2):
        # print the specail group
        groupWantSearch = sys.argv[1].upper() 
        if (groupWantSearch in ALLGROUP.keys()):
            swList += [groupWantSearch]
        else:
            # print usage info
            print('The group name ' + sys.argv[1] + ' not correct or not in list...')
    else:
        # print usage info
        print('usage:>>>python PRGroup.py group_name')
        print('group_name: e.g. TDDMACPS/UEC/CLEEC')
        
    printInfo(swList)

if __name__ == '__main__':
    main()