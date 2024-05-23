from collections import Counter

data1 = "ITERATION 1:  ITERATION 2:  destroy 4 repair 3 ITERATION 3:  ITERATION 4:  ITERATION 5:  destroy 4 repair 3 destroy 0 repair 3 ITERATION 6:  destroy 0 repair 1 destroy 4 repair 3 destroy 0 repair 3 ITERATION 7:  destroy 0 repair 3 ITERATION 8:  ITERATION 9:  destroy 4 repair 3 ITERATION 10:  ITERATION 11:  destroy 10 repair 2 ITERATION 12:  destroy 0 repair 3 ITERATION 13:  ITERATION 14:  destroy 0 repair 1 ITERATION 15:  ITERATION 16:  destroy 10 repair 2 destroy 4 repair 3 ITERATION 17:  destroy 0 repair 1 ITERATION 18:  ITERATION 19:  destroy 4 repair 3 ITERATION 20:  ITERATION 21:  destroy 4 repair 3 ITERATION 22:  ITERATION 23:  ITERATION 24:  ITERATION 25:  destroy 4 repair 3 ITERATION 26:  ITERATION 27:  ITERATION 28:  ITERATION 29:  destroy 0 repair 1 ITERATION 30:  ITERATION 31:  ITERATION 32:  destroy 4 repair 3 destroy 10 repair 2 ITERATION 33:  ITERATION 34:  destroy 4 repair 3 destroy 10 repair 3 ITERATION 35:  destroy 10 repair 3 ITERATION 36:  ITERATION 37:  ITERATION 38:  destroy 10 repair 2 ITERATION 39:  ITERATION 40:  ITERATION 41:  destroy 0 repair 1 destroy 10 repair 2 ITERATION 42:  destroy 0 repair 3 ITERATION 43:  ITERATION 44:  destroy 0 repair 1 destroy 4 repair 3 ITERATION 45:  ITERATION 46:  ITERATION 47:  destroy 10 repair 2 ITERATION 48:  ITERATION 49:  ITERATION 50:  destroy 10 repair 3 destroy 10 repair 2 ITERATION 51:  ITERATION 52:  destroy 10 repair 3 destroy 10 repair 2 ITERATION 53:  ITERATION 54:  ITERATION 55:  destroy 10 repair 2 destroy 0 repair 3 destroy 10 repair 3 ITERATION 56:  ITERATION 57:  ITERATION 58:  destroy 0 repair 1 ITERATION 59:  ITERATION 60:  destroy 4 repair 3 destroy 10 repair 2 ITERATION 61:  ITERATION 62:  ITERATION 63:  destroy 4 repair 3 ITERATION 64:  ITERATION 65:  destroy 4 repair 3ALNS iteration 65 is new global best, objective [42, 58, -16, 773] BestDestroy4 BestRepair3"
data2 = "ITERATION 66:  ITERATION 67:  ITERATION 68:  ITERATION 69:  ITERATION 70:  ITERATION 71:  destroy 0 repair 1 destroy 0 repair 3 destroy 4 repair 3 ITERATION 72:  ITERATION 73:  destroy 4 repair 3 ITERATION 74:  destroy 4 repair 3 ITERATION 75:  ITERATION 76:  destroy 0 repair 1 ITERATION 77:  ITERATION 78:  destroy 0 repair 1 ITERATION 79:  ITERATION 80:  ITERATION 81:  destroy 4 repair 3 destroy 10 repair 3 destroy 10 repair 2 destroy 0 repair 3 ITERATION 82:  ITERATION 83:  destroy 10 repair 3 destroy 10 repair 2 ITERATION 84:  destroy 0 repair 1 destroy 4 repair 3 ITERATION 85:  ITERATION 86:  destroy 10 repair 2 destroy 0 repair 3 destroy 10 repair 3 destroy 4 repair 3 ITERATION 87:  ITERATION 88:  destroy 0 repair 3 destroy 4 repair 3 ITERATION 89:  destroy 10 repair 3 ITERATION 90:  ITERATION 91:  destroy 0 repair 1 destroy 10 repair 3 destroy 4 repair 3 ITERATION 92:  destroy 0 repair 1 destroy 4 repair 3 destroy 0 repair 3 ITERATION 93:  ITERATION 94:  destroy 10 repair 3 destroy 0 repair 3 destroy 0 repair 1 ITERATION 95:  destroy 4 repair 3 ITERATION 96:  ITERATION 97:  destroy 0 repair 3 ITERATION 98:  ITERATION 99:  ITERATION 100:  destroy 4 repair 3"
data3 = ""

data1 ="ITERATION 1:  destroy 8 repair 0ALNS iteration 1 is new global best, objective [41, 46, -24, 507] BestDestroy8 BestRepair0"
data2 =  "ITERATION 2:  destroy 7 repair 0 destroy 7 repair 1 destroy 9 repair 2 destroy 12 repair 3ALNS iteration 2 is new global best, objective [45, 57, -26, 601] BestDestroy12 BestRepair3"
data3 =  "ITERATION 3:  ITERATION 4:  ITERATION 5:  ITERATION 6:  destroy 4 repair 1 ITERATION 7:  destroy 4 repair 1 ITERATION 8:  ITERATION 9:  destroy 12 repair 3 ITERATION 10:  destroy 12 repair 3 ITERATION 11:  ITERATION 12:  destroy 8 repair 0 destroy 13 repair 3 ITERATION 13:  destroy 12 repair 3 destroy 5 repair 2 ITERATION 14:  ITERATION 15:  ITERATION 16:  destroy 4 repair 1 ITERATION 17:  destroy 4 repair 1 destroy 8 repair 0 ITERATION 18:  ITERATION 19:  ITERATION 20:  destroy 12 repair 3 destroy 13 repair 3 ITERATION 21:  destroy 12 repair 3 ITERATION 22:  destroy 4 repair 1 ITERATION 23:  ITERATION 24:  ITERATION 25:  ITERATION 26:  destroy 4 repair 1 ITERATION 27:  ITERATION 28:  destroy 13 repair 3 destroy 5 repair 2 ITERATION 29:  destroy 8 repair 0 ITERATION 30:  ITERATION 31:  ITERATION 32:  destroy 4 repair 1 destroy 5 repair 2 ITERATION 33:  destroy 4 repair 1 destroy 8 repair 0 ITERATION 34:  ITERATION 35:  ITERATION 36:  destroy 8 repair 0 ITERATION 37:  ITERATION 38:  destroy 4 repair 1 destroy 12 repair 3 ITERATION 39:  destroy 8 repair 0 ITERATION 40:  destroy 4 repair 1 destroy 13 repair 3 destroy 12 repair 3 ITERATION 41:  ITERATION 42:  ITERATION 43:  ITERATION 44:  ITERATION 45:  destroy 5 repair 2 destroy 4 repair 1 ITERATION 46:  ITERATION 47:  destroy 8 repair 0 ITERATION 48:  ITERATION 49:  ITERATION 50:  destroy 4 repair 1 ITERATION 51:  ITERATION 52:  ITERATION 53:  destroy 13 repair 3 ITERATION 54:  destroy 4 repair 1 ITERATION 55:  destroy 4 repair 1 ITERATION 56:  destroy 5 repair 2 ITERATION 57:  ITERATION 58:  destroy 4 repair 1 destroy 12 repair 3 destroy 8 repair 0 ITERATION 59:  ITERATION 60:  ITERATION 61:  destroy 4 repair 1 destroy 13 repair 3 ITERATION 62:  destroy 12 repair 3 ITERATION 63:  ITERATION 64:  ITERATION 65:  destroy 4 repair 1 destroy 5 repair 2 ITERATION 66:  ITERATION 67:  ITERATION 68:  destroy 5 repair 2 destroy 13 repair 3 ITERATION 69:  destroy 4 repair 1 ITERATION 70:  ITERATION 71:  destroy 8 repair 0 destroy 12 repair 3 ITERATION 72:  ITERATION 73:  ITERATION 74:  ITERATION 75:  ITERATION 76:  ITERATION 77:  destroy 4 repair 1 ITERATION 78:  destroy 4 repair 1 destroy 8 repair 0 destroy 5 repair 2 ITERATION 79:  ITERATION 80:  ITERATION 81:  destroy 4 repair 1 destroy 13 repair 3 ITERATION 82:  destroy 5 repair 2 ITERATION 83:  ITERATION 84:  ITERATION 85:  destroy 13 repair 3 ITERATION 86:  ITERATION 87:  ITERATION 88:  destroy 13 repair 3 ITERATION 89:  ITERATION 90:  destroy 4 repair 1 destroy 8 repair 0 ITERATION 91:  ITERATION 92:  ITERATION 93:  destroy 12 repair 3 ITERATION 94:  ITERATION 95:  destroy 5 repair 2 ITERATION 96:  ITERATION 97:  ITERATION 98:  destroy 4 repair 1 destroy 5 repair 2 ITERATION 99:  ITERATION 100:  destroy 13 repair 3 destroy 5 repair 2"


data1 = "ITERATION 1:  ITERATION 2:  destroy 14 repair 0 destroy 10 repair 1 destroy 14 repair 2 destroy 8 repair 2 destroy 5 repair 2 destroy 4 repair 2 ITERATION 3:  ITERATION 4:  destroy 14 repair 0 destroy 5 repair 3 destroy 5 repair 2 destroy 4 repair 2 ITERATION 5:  destroy 14 repair 2 destroy 10 repair 1ALNS iteration 5 is new global best, objective [33, 60, -23, 714] BestDestroy14 BestRepair2"
data2 =  "ITERATION 6:  ITERATION 7:  ITERATION 8:  ITERATION 9:  destroy 14 repair 2 destroy 5 repair 3 ITERATION 10:  ITERATION 11:  ITERATION 12:  destroy 10 repair 1 destroy 5 repair 2 ITERATION 13:  destroy 14 repair 2 ITERATION 14:  destroy 14 repair 0 destroy 14 repair 2 destroy 4 repair 2 ITERATION 15:  ITERATION 16:  ITERATION 17:  destroy 14 repair 2 ITERATION 18:  destroy 14 repair 2 ITERATION 19:  destroy 14 repair 2 destroy 4 repair 2 destroy 10 repair 1 ITERATION 20:  destroy 10 repair 1 ITERATION 21:  destroy 5 repair 2 destroy 4 repair 2 ITERATION 22:  ITERATION 23:  destroy 14 repair 2 destroy 5 repair 3 destroy 4 repair 2 destroy 5 repair 2 ITERATION 24:  destroy 14 repair 0 destroy 14 repair 2 destroy 5 repair 3 destroy 5 repair 2 destroy 4 repair 2 ITERATION 25:  ITERATION 26:  destroy 14 repair 0 destroy 14 repair 2 ITERATION 27:  ITERATION 28:  ITERATION 29:  destroy 8 repair 2 ITERATION 30:  ITERATION 31:  ITERATION 32:  ITERATION 33:  destroy 14 repair 2 destroy 8 repair 2 ITERATION 34:  ITERATION 35:  destroy 14 repair 2 destroy 10 repair 1 destroy 5 repair 3 destroy 8 repair 2 destroy 5 repair 2 ITERATION 36:  ITERATION 37:  destroy 4 repair 2 ITERATION 38:  ITERATION 39:  ITERATION 40:  destroy 14 repair 0 ITERATION 41:  destroy 14 repair 0 destroy 8 repair 2 ITERATION 42:  ITERATION 43:  ITERATION 44:  destroy 4 repair 2 ITERATION 45:  destroy 14 repair 0 destroy 5 repair 3 destroy 10 repair 1 ITERATION 46:  ITERATION 47:  destroy 14 repair 0 ITERATION 48:  destroy 8 repair 2 ITERATION 49:  ITERATION 50:  ITERATION 51:  destroy 14 repair 2 destroy 10 repair 1 ITERATION 52:  ITERATION 53:  ITERATION 54:  ITERATION 55:  destroy 14 repair 2 ITERATION 56:  destroy 5 repair 3 destroy 4 repair 2 ITERATION 57:  destroy 14 repair 2 ITERATION 58:  ITERATION 59:  destroy 8 repair 2 ITERATION 60:  ITERATION 61:  ITERATION 62:  destroy 14 repair 2 destroy 5 repair 3 destroy 5 repair 2 destroy 4 repair 2 ITERATION 63:  destroy 14 repair 0 ITERATION 64:  ITERATION 65:  destroy 14 repair 2 destroy 10 repair 1 destroy 8 repair 2 ITERATION 66:  destroy 5 repair 2 ITERATION 67:  destroy 14 repair 2 destroy 10 repair 1 destroy 5 repair 2 ITERATION 68:  destroy 14 repair 2 destroy 8 repair 2 ITERATION 69:  destroy 14 repair 2 destroy 10 repair 1 destroy 8 repair 2 ITERATION 70:  destroy 10 repair 1 ITERATION 71:  destroy 8 repair 2 ITERATION 72:  ITERATION 73:  ITERATION 74:  ITERATION 75:  ITERATION 76:  ITERATION 77:  ITERATION 78:  ITERATION 79:  ITERATION 80:  destroy 8 repair 2 ITERATION 81:  ITERATION 82:  ITERATION 83:  destroy 14 repair 0 destroy 5 repair 2 destroy 5 repair 3 destroy 4 repair 2 ITERATION 84:  destroy 14 repair 2 ITERATION 85:  destroy 4 repair 2 ITERATION 86:  ITERATION 87:  ITERATION 88:  destroy 14 repair 0 destroy 10 repair 1 destroy 4 repair 2 destroy 5 repair 2 destroy 5 repair 3 destroy 14 repair 2 destroy 8 repair 2 ITERATION 89:  ITERATION 90:  destroy 10 repair 1 destroy 5 repair 3 destroy 5 repair 2 ITERATION 91:  ITERATION 92:  ITERATION 93:  ITERATION 94:  destroy 14 repair 2 destroy 14 repair 0 ITERATION 95:  ITERATION 96:  destroy 14 repair 0 destroy 8 repair 2 ITERATION 97:  ITERATION 98:  destroy 14 repair 2 ITERATION 99:  destroy 10 repair 1 destroy 14 repair 0 destroy 4 repair 2 destroy 5 repair 2 destroy 8 repair 2 ITERATION 100:"
data3 = ""
'''
'''

data1 = "ITERATION 1:  ITERATION 2:  ITERATION 3:  destroy 2 repair 1 destroy 2 repair 1 destroy 5 repair 0 destroy 5 repair 1 ITERATION 4:  ITERATION 5:  destroy 9 repair 3 ITERATION 6:  destroy 2 repair 1 destroy 2 repair 1 destroy 5 repair 0 ITERATION 7:  ITERATION 8:  ITERATION 9:  ITERATION 10:  destroy 5 repair 1 destroy 5 repair 0 ITERATION 11:  destroy 2 repair 1 destroy 2 repair 1 ITERATION 12:  ITERATION 13:  ITERATION 14:  ITERATION 15:  ITERATION 16:  ITERATION 17:  ITERATION 18:  ITERATION 19:  ITERATION 20:  destroy 5 repair 1 destroy 5 repair 0 ITERATION 21:  ITERATION 22:  destroy 5 repair 1 destroy 5 repair 0 ITERATION 23:  ITERATION 24:  ITERATION 25:  destroy 5 repair 1 destroy 2 repair 1 destroy 2 repair 1 ITERATION 26:  ITERATION 27:  ITERATION 28:  destroy 12 repair 1 ITERATION 29:  destroy 8 repair 1 ITERATION 30:  destroy 5 repair 1 ITERATION 31:  ITERATION 32:  ITERATION 33:  destroy 5 repair 0 destroy 8 repair 2 ITERATION 34:  destroy 12 repair 1 destroy 2 repair 1 destroy 8 repair 1 destroy 2 repair 1 destroy 5 repair 1 ITERATION 35:  ITERATION 36:  ITERATION 37:  destroy 5 repair 1 ITERATION 38:  ITERATION 39:  destroy 8 repair 1 destroy 8 repair 2 ITERATION 40:  ITERATION 41:  ITERATION 42:  ITERATION 43:  ITERATION 44:  destroy 5 repair 1 ITERATION 45:  destroy 8 repair 1 destroy 8 repair 2 ITERATION 46:  destroy 12 repair 1 ITERATION 47:  destroy 2 repair 1 destroy 2 repair 1 destroy 8 repair 2ALNS iteration 47 is new global best, objective [114, 111, -28, 1750] BestDestroy8 BestRepair2"
data2 = "ITERATION 48:  ITERATION 49:  ITERATION 50:  ITERATION 51:  ITERATION 52:  destroy 2 repair 1 destroy 2 repair 1 destroy 5 repair 1 destroy 8 repair 2 ITERATION 53:  ITERATION 54:  ITERATION 55:  ITERATION 56:  destroy 5 repair 1 destroy 8 repair 1 ITERATION 57:  destroy 8 repair 1 destroy 5 repair 0 destroy 5 repair 1 destroy 8 repair 2ALNS iteration 57 is new global best, objective [115, 106, -36, 1704] BestDestroy8 BestRepair2"
data3 = "ITERATION 58:  ITERATION 59:  destroy 5 repair 1 ITERATION 60:  ITERATION 61:  destroy 5 repair 1 ITERATION 62:  destroy 5 repair 1 destroy 5 repair 0ALNS iteration 62 is new global best, objective [117, 112, -32, 1812] BestDestroy5 BestRepair0"
data4 = "ITERATION 63:  ITERATION 64:  destroy 5 repair 0 ITERATION 65:  ITERATION 66:  destroy 5 repair 1ALNS iteration 66 is new global best, objective [117, 108, -28, 1733] BestDestroy5 BestRepair1"
data5 = "ITERATION 67:  ITERATION 68:  ITERATION 69:  ITERATION 70:  destroy 5 repair 0 ITERATION 71:  destroy 5 repair 1 ITERATION 72:  destroy 8 repair 2 ITERATION 73:  ITERATION 74:  destroy 5 repair 0 ITERATION 75:  ITERATION 76:  destroy 5 repair 0 ITERATION 77:  ITERATION 78:  ITERATION 79:  ITERATION 80:  destroy 2 repair 1 destroy 2 repair 1 ITERATION 81:  ITERATION 82:  destroy 5 repair 1 ITERATION 83:  destroy 12 repair 1 destroy 5 repair 1 ITERATION 84:  destroy 12 repair 1 ITERATION 85:  ITERATION 86:  ITERATION 87:  ITERATION 88:  destroy 5 repair 0 destroy 5 repair 1 ITERATION 89:  ITERATION 90:  destroy 12 repair 1 ITERATION 91:  ITERATION 92:  ITERATION 93:  ITERATION 94:  destroy 12 repair 1 ITERATION 95:  ITERATION 96:  destroy 5 repair 0 destroy 5 repair 1 ITERATION 97:  destroy 8 repair 1 ITERATION 98:  ITERATION 99:  destroy 5 repair 1 ITERATION 100:  destroy 12 repair 1"
data = data1 + data2 + data3 + data4 + data5

data = '''
ITERATION 1:  destroy 13 repair 2ALNS iteration 1 is new global best, objective [65, 62, -38, 1150] BestDestroy13 BestRepair2
 ITERATION 2:  ITERATION 3:  destroy 13 repair 2ALNS iteration 3 is new global best, objective [69, 67, -39, 1252] BestDestroy13 BestRepair2
 ITERATION 4:  ITERATION 5:  destroy 1 repair 3 ITERATION 6:  ITERATION 7:  ITERATION 8:  ITERATION 9:  ITERATION 10:  ITERATION 11:  destroy 10 repair 1 destroy 13 repair 1 destroy 13 repair 2 ITERATION 12:  destroy 10 repair 1 destroy 13 repair 1 ITERATION 13:  ITERATION 14:  ITERATION 15:  destroy 10 repair 1 ITERATION 16:  destroy 13 repair 1 ITERATION 17:  destroy 13 repair 1 destroy 1 repair 3ALNS iteration 17 is new global best, objective [70, 61, -35, 1181] BestDestroy13 BestRepair1
 ITERATION 18:  ITERATION 19:  ITERATION 20:  ITERATION 21:  ITERATION 22:  ITERATION 23:  ITERATION 24:  destroy 13 repair 1 ITERATION 25:  ITERATION 26:  ITERATION 27:  ITERATION 28:  ITERATION 29:  ITERATION 30:  destroy 10 repair 1 ITERATION 31:  destroy 10 repair 1 destroy 13 repair 1 ITERATION 32:  destroy 13 repair 1ALNS iteration 32 is new global best, objective [72, 67, -35, 1169] BestDestroy13 BestRepair1
 ITERATION 33:  ITERATION 34:  ITERATION 35:  ITERATION 36:  ITERATION 37:  ITERATION 38:  destroy 13 repair 2 ITERATION 39:  ITERATION 40:  ITERATION 41:  ITERATION 42:  destroy 1 repair 0 destroy 10 repair 1 destroy 0 repair 3 destroy 0 repair 2 ITERATION 43:  ITERATION 44:  ITERATION 45:  ITERATION 46:  destroy 10 repair 1 ITERATION 47:  destroy 1 repair 0 destroy 1 repair 3 destroy 0 repair 2 ITERATION 48:  ITERATION 49:  ITERATION 50:  destroy 13 repair 1 ITERATION 51:  ITERATION 52:  destroy 10 repair 1 ITERATION 53:  ITERATION 54:  ITERATION 55:  destroy 10 repair 1 destroy 13 repair 2 ITERATION 56:  ITERATION 57:  destroy 13 repair 2 ITERATION 58:  ITERATION 59:  ITERATION 60:  destroy 0 repair 2 ITERATION 61:  ITERATION 62:  destroy 10 repair 1 ITERATION 63:  ITERATION 64:  destroy 10 repair 1 ITERATION 65:  destroy 10 repair 1 ITERATION 66:  destroy 13 repair 2 ITERATION 67:  destroy 10 repair 1 ITERATION 68:  destroy 13 repair 2 ITERATION 69:  ITERATION 70:  ITERATION 71:  ITERATION 72:  ITERATION 73:  destroy 13 repair 2 ITERATION 74:  ITERATION 75:  destroy 13 repair 2 ITERATION 76:  ITERATION 77:  destroy 13 repair 1 ITERATION 78:  ITERATION 79:  destroy 13 repair 1 ITERATION 80:  destroy 13 repair 2 ITERATION 81:  destroy 13 repair 2 ITERATION 82:  ITERATION 83:  ITERATION 84:  destroy 13 repair 1 ITERATION 85:  destroy 13 repair 1 destroy 13 repair 2 ITERATION 86:  destroy 10 repair 1 destroy 13 repair 1 destroy 13 repair 2 ITERATION 87:  destroy 1 repair 0 destroy 1 repair 3 destroy 0 repair 3 destroy 0 repair 2 ITERATION 88:  destroy 13 repair 2 ITERATION 89:  ITERATION 90:  destroy 13 repair 1 ITERATION 91:  destroy 1 repair 0 destroy 1 repair 3 destroy 0 repair 2 ITERATION 92:  destroy 13 repair 2 ITERATION 93:  destroy 13 repair 1 ITERATION 94:  ITERATION 95:  destroy 13 repair 2 ITERATION 96:  destroy 1 repair 3 destroy 0 repair 2 ITERATION 97:  destroy 13 repair 1 ITERATION 98:  destroy 13 repair 2 ITERATION 99:  ITERATION 100:  destroy 13 repair 2
'''
data = '''
ITERATION 1: ALNS iteration 1 is new global best, objective [65, 57, -30, 935] BestDestroy0 BestRepair1
 ITERATION 2:  destroy 2 repair 3 destroy 2 repair 2 ITERATION 3:  ITERATION 4:  ITERATION 5:  ITERATION 6:  ITERATION 7:  destroy 0 repair 1 destroy 2 repair 3 destroy 1 repair 3 destroy 2 repair 2 ITERATION 8:  ITERATION 9:  destroy 2 repair 3 destroy 2 repair 2 ITERATION 10:  ITERATION 11:  ITERATION 12:  ITERATION 13:  ITERATION 14:  destroy 1 repair 3 ITERATION 15:  destroy 0 repair 1 destroy 1 repair 3 ITERATION 16:  destroy 0 repair 1 destroy 1 repair 3ALNS iteration 16 is new global best, objective [66, 64, -28, 1049] BestDestroy1 BestRepair3
 ITERATION 17:  ITERATION 18:  ITERATION 19:  destroy 0 repair 1 destroy 9 repair 3 destroy 2 repair 3 destroy 1 repair 3 destroy 2 repair 2ALNS iteration 19 is new global best, objective [69, 67, -30, 1010] BestDestroy0 BestRepair1
 ITERATION 20:  ITERATION 21:  destroy 0 repair 1 ITERATION 22:  ITERATION 23:  ITERATION 24:  ITERATION 25:  ITERATION 26:  ITERATION 27:  ITERATION 28:  destroy 2 repair 3 destroy 1 repair 3 destroy 2 repair 2 ITERATION 29:  destroy 0 repair 1 destroy 1 repair 3 ITERATION 30:  destroy 1 repair 3 ITERATION 31:  ITERATION 32:  ITERATION 33:  destroy 9 repair 3 ITERATION 34:  destroy 2 repair 3 destroy 2 repair 2 ITERATION 35:  ITERATION 36:  ITERATION 37:  ITERATION 38:  ITERATION 39:  destroy 0 repair 1 ITERATION 40:  ITERATION 41:  ITERATION 42:  destroy 0 repair 1 destroy 2 repair 3 destroy 2 repair 2 ITERATION 43:  destroy 0 repair 1 destroy 1 repair 3 ITERATION 44:  destroy 0 repair 1 destroy 2 repair 3 destroy 2 repair 2 ITERATION 45:  ITERATION 46:  ITERATION 47:  ITERATION 48:  ITERATION 49:  destroy 1 repair 3 ITERATION 50:  ITERATION 51:  ITERATION 52:  destroy 0 repair 1 destroy 1 repair 3 ITERATION 53:  ITERATION 54:  destroy 1 repair 3 ITERATION 55:  destroy 0 repair 1 ITERATION 56:  destroy 2 repair 2 ITERATION 57:  destroy 2 repair 3 destroy 2 repair 2 ITERATION 58:  ITERATION 59:  ITERATION 60:  ITERATION 61:  ITERATION 62:  destroy 1 repair 3 ITERATION 63:  destroy 0 repair 1 destroy 2 repair 3 destroy 2 repair 2 ITERATION 64:  destroy 0 repair 1 destroy 9 repair 3 destroy 2 repair 3 destroy 1 repair 3 destroy 2 repair 2 ITERATION 65:  ITERATION 66:  ITERATION 67:  destroy 0 repair 1 ITERATION 68:  ITERATION 69:  destroy 0 repair 1 destroy 2 repair 3 destroy 1 repair 3 destroy 2 repair 2 ITERATION 70:  ITERATION 71:  destroy 0 repair 1 destroy 2 repair 3 destroy 1 repair 3 destroy 2 repair 2 ITERATION 72:  destroy 0 repair 1 destroy 2 repair 2 ITERATION 73:  ITERATION 74:  ITERATION 75:  ITERATION 76:  ITERATION 77:  ITERATION 78:  ITERATION 79:  ITERATION 80:  destroy 0 repair 1 destroy 1 repair 3 ITERATION 81:  destroy 1 repair 3 ITERATION 82:  ITERATION 83:  ITERATION 84:  destroy 2 repair 3 destroy 2 repair 2 ITERATION 85:  ITERATION 86:  ITERATION 87:  ITERATION 88:  destroy 2 repair 3 destroy 2 repair 2 ITERATION 89:  ITERATION 90:  ITERATION 91:  destroy 0 repair 1 destroy 2 repair 3 destroy 1 repair 3 destroy 2 repair 2 ITERATION 92:  destroy 2 repair 3 destroy 2 repair 2 ITERATION 93:  ITERATION 94:  ITERATION 95:  destroy 0 repair 1 destroy 1 repair 3 ITERATION 96:  ITERATION 97:  ITERATION 98:  destroy 0 repair 1 destroy 1 repair 3 ITERATION 99:  destroy 0 repair 1 ITERATION 100:  destroy 0 repair 1
'''

data = '''
ITERATION 1:  destroy 7 repair 3 destroy 4 repair 2 destroy 14 repair 2 destroy 14 repair 2 destroy 10 repair 2 ITERATION 2:  ITERATION 3:  destroy 14 repair 0 ITERATION 4:  ITERATION 5:  ITERATION 6:  ITERATION 7:  ITERATION 8:  destroy 14 repair 2 ITERATION 9:  ITERATION 10:  ITERATION 11: ALNS iteration 11 is new global best, objective [65, 55, -23, 971] BestDestroy4 BestRepair2
 ITERATION 12:  destroy 4 repair 0 destroy 8 repair 1 destroy 4 repair 2 destroy 14 repair 2ALNS iteration 12 is new global best, objective [67, 60, -19, 1028] BestDestroy4 BestRepair0
 ITERATION 13:  ITERATION 14:  ITERATION 15:  destroy 14 repair 0 destroy 14 repair 2 destroy 4 repair 2ALNS iteration 15 is new global best, objective [69, 67, -20, 963] BestDestroy4 BestRepair2
 ITERATION 16:  destroy 14 repair 2 ITERATION 17:  ITERATION 18:  ITERATION 19:  ITERATION 20:  ITERATION 21:  ITERATION 22:  ITERATION 23:  destroy 14 repair 2 ITERATION 24:  ITERATION 25:  destroy 14 repair 2 destroy 14 repair 2 ITERATION 26:  ITERATION 27:  ITERATION 28:  ITERATION 29:  ITERATION 30:  ITERATION 31:  destroy 14 repair 2 ITERATION 32:  ITERATION 33:  destroy 4 repair 0 destroy 14 repair 2 destroy 14 repair 2 destroy 10 repair 2 destroy 4 repair 2 ITERATION 34:  ITERATION 35:  destroy 10 repair 2 ITERATION 36:  ITERATION 37:  ITERATION 38:  ITERATION 39:  ITERATION 40:  destroy 10 repair 2 ITERATION 41:  ITERATION 42:  destroy 14 repair 0 ITERATION 43:  destroy 10 repair 2 ITERATION 44:  ITERATION 45:  destroy 4 repair 0 destroy 14 repair 2 destroy 10 repair 2 destroy 4 repair 2 ITERATION 46:  destroy 8 repair 1ALNS iteration 46 is new global best, objective [72, 65, -15, 986] BestDestroy8 BestRepair1
 ITERATION 47:  ITERATION 48:  ITERATION 49:  ITERATION 50:  ITERATION 51:  destroy 4 repair 0 destroy 14 repair 0 destroy 8 repair 1 destroy 10 repair 2 destroy 4 repair 2 ITERATION 52:  destroy 4 repair 0 destroy 14 repair 2 destroy 10 repair 2 ITERATION 53:  ITERATION 54:  ITERATION 55:  ITERATION 56:  destroy 4 repair 0 destroy 4 repair 2 ITERATION 57:  ITERATION 58:  destroy 14 repair 2 ITERATION 59:  destroy 14 repair 2 ITERATION 60:  ITERATION 61:  ITERATION 62:  destroy 10 repair 2 ITERATION 63:  ITERATION 64:  destroy 8 repair 1 destroy 4 repair 0 destroy 4 repair 2 destroy 8 repair 2 ITERATION 65:  ITERATION 66:  destroy 14 repair 2 ITERATION 67:  ITERATION 68:  destroy 4 repair 0 destroy 10 repair 2 destroy 4 repair 2 ITERATION 69:  ITERATION 70:  ITERATION 71:  destroy 14 repair 0 destroy 14 repair 2 destroy 14 repair 2 ITERATION 72:  ITERATION 73:  ITERATION 74:  destroy 8 repair 0 destroy 8 repair 1 destroy 14 repair 0 destroy 8 repair 2 ITERATION 75:  ITERATION 76:  ITERATION 77:  destroy 8 repair 1 ITERATION 78:  ITERATION 79:  destroy 4 repair 0 destroy 8 repair 0 destroy 4 repair 2 destroy 8 repair 2 destroy 14 repair 2 ITERATION 80:  destroy 4 repair 0 destroy 8 repair 0 destroy 4 repair 2 destroy 8 repair 2 ITERATION 81:  ITERATION 82:  ITERATION 83:  ITERATION 84:  destroy 14 repair 0 ITERATION 85:  destroy 14 repair 0 ITERATION 86:  ITERATION 87:  ITERATION 88:  destroy 4 repair 0 ITERATION 89:  ITERATION 90:  ITERATION 91:  destroy 14 repair 2 ITERATION 92:  ITERATION 93:  destroy 4 repair 0 destroy 4 repair 2 ITERATION 94:  destroy 4 repair 0 destroy 4 repair 2 ITERATION 95:  ITERATION 96:  ITERATION 97:  destroy 8 repair 1 ITERATION 98:  destroy 4 repair 0 destroy 14 repair 0 destroy 14 repair 2 destroy 14 repair 2 destroy 4 repair 2 ITERATION 99:  destroy 14 repair 2 ITERATION 100: 
'''
data = '''
ITERATION 1:  ITERATION 2:  destroy 2 repair 0 destroy 12 repair 0 destroy 0 repair 1 destroy 2 repair 2 ITERATION 3:  ITERATION 4:  ITERATION 5:  destroy 13 repair 1 ITERATION 6:  ITERATION 7:  destroy 13 repair 1 destroy 0 repair 1 destroy 2 repair 0 destroy 2 repair 2 ITERATION 8:  destroy 2 repair 0 destroy 2 repair 2 ITERATION 9:  destroy 10 repair 2 ITERATION 10: ALNS iteration 10 is new global best, objective [110, 70, -27, 1452] BestDestroy8 BestRepair1
 ITERATION 11: ALNS iteration 11 is new global best, objective [110, 69, -26, 1475] BestDestroy0 BestRepair1
 ITERATION 12:  ITERATION 13:  destroy 2 repair 0 destroy 2 repair 2 ITERATION 14:  ITERATION 15:  ITERATION 16:  ITERATION 17:  ITERATION 18:  destroy 2 repair 0 destroy 2 repair 2 ITERATION 19:  ITERATION 20:  ITERATION 21:  ITERATION 22:  destroy 13 repair 1 ITERATION 23:  ITERATION 24:  ITERATION 25:  ITERATION 26:  ITERATION 27:  ITERATION 28:  ITERATION 29:  destroy 0 repair 1 destroy 13 repair 1 ITERATION 30:  ITERATION 31:  ITERATION 32:  destroy 2 repair 0 destroy 2 repair 2 ITERATION 33:  destroy 13 repair 1 ITERATION 34:  ITERATION 35:  ITERATION 36:  ITERATION 37:  ITERATION 38:  destroy 13 repair 1
'''

data = '''
ITERATION 1:  destroy 7 repair 1 destroy 7 repair 0 destroy 0 repair 0 destroy 4 repair 0 destroy 4 repair 3 destroy 6 repair 2 destroy 6 repair 2ALNS iteration 1 is new global best, objective [114, 98, -25, 1655] BestDestroy0 BestRepair0
 ITERATION 2:  destroy 9 repair 1 ITERATION 3:  destroy 9 repair 1 ITERATION 4:  destroy 7 repair 0 destroy 9 repair 1 ITERATION 5:  destroy 9 repair 1 ITERATION 6:  destroy 9 repair 1 ITERATION 7:  destroy 9 repair 1 ITERATION 8:  ITERATION 9:  ITERATION 10:  destroy 9 repair 1 ITERATION 11:  ITERATION 12:  ITERATION 13:  ITERATION 14:  ITERATION 15:  ITERATION 16:  ITERATION 17:  destroy 0 repair 0 ITERATION 18:  destroy 0 repair 0 destroy 4 repair 0 destroy 4 repair 3 ITERATION 19:  ITERATION 20:  ITERATION 21:  destroy 0 repair 0 ITERATION 22:  ITERATION 23:  ITERATION 24:  ITERATION 25:  ITERATION 26:  destroy 9 repair 1 ITERATION 27:  destroy 0 repair 0 destroy 4 repair 0 destroy 0 repair 0 destroy 4 repair 3 ITERATION 28:  ITERATION 29:  ITERATION 30:  ITERATION 31:  ITERATION 32:  ITERATION 33:  destroy 0 repair 0 ITERATION 34:  destroy 9 repair 1 destroy 0 repair 0 destroy 0 repair 0 destroy 4 repair 0 destroy 4 repair 3 ITERATION 35:  ITERATION 36:  ITERATION 37:  ITERATION 38:  destroy 0 repair 0 destroy 4 repair 3 ITERATION 39:  ITERATION 40:  destroy 0 repair 0 destroy 0 repair 0 ITERATION 41:  ITERATION 42:  ITERATION 43:  destroy 0 repair 0 destroy 0 repair 0 ITERATION 44:  destroy 4 repair 0 ITERATION 45:  ITERATION 46:  destroy 0 repair 0 destroy 0 repair 0 ITERATION 47:  destroy 0 repair 0 destroy 0 repair 0 ITERATION 48:  destroy 0 repair 0 ITERATION 49: 
'''

data ='''
ITERATION 1:  destroy 7 repair 1 destroy 7 repair 0 destroy 0 repair 0 destroy 4 repair 0 destroy 4 repair 3 destroy 6 repair 2 destroy 6 repair 2ALNS iteration 1 is new global best, objective [114, 98, -25, 1655] BestDestroy0 BestRepair0
 ITERATION 2:  destroy 9 repair 1 ITERATION 3:  destroy 9 repair 1 ITERATION 4:  destroy 7 repair 0 destroy 9 repair 1 ITERATION 5:  destroy 9 repair 1 ITERATION 6:  destroy 9 repair 1 ITERATION 7:  destroy 9 repair 1 ITERATION 8:  ITERATION 9:  ITERATION 10:  destroy 9 repair 1 ITERATION 11:  ITERATION 12:  ITERATION 13:  ITERATION 14:  ITERATION 15:  ITERATION 16:  ITERATION 17:  destroy 0 repair 0 ITERATION 18:  destroy 0 repair 0 destroy 4 repair 0 destroy 4 repair 3 ITERATION 19:  ITERATION 20:  ITERATION 21:  destroy 0 repair 0 ITERATION 22:  ITERATION 23:  ITERATION 24:  ITERATION 25:  ITERATION 26:  destroy 9 repair 1 ITERATION 27:  destroy 0 repair 0 destroy 4 repair 0 destroy 0 repair 0 destroy 4 repair 3 ITERATION 28:  ITERATION 29:  ITERATION 30:  ITERATION 31:  ITERATION 32:  ITERATION 33:  destroy 0 repair 0 ITERATION 34:  destroy 9 repair 1 destroy 0 repair 0 destroy 0 repair 0 destroy 4 repair 0 destroy 4 repair 3 ITERATION 35:  ITERATION 36:  ITERATION 37:  ITERATION 38:  destroy 0 repair 0 destroy 4 repair 3 ITERATION 39:  ITERATION 40:  destroy 0 repair 0 destroy 0 repair 0 ITERATION 41:  ITERATION 42:  ITERATION 43:  destroy 0 repair 0 destroy 0 repair 0 ITERATION 44:  destroy 4 repair 0 ITERATION 45:  ITERATION 46:  destroy 0 repair 0 destroy 0 repair 0 ITERATION 47:  destroy 0 repair 0 destroy 0 repair 0 ITERATION 48:  destroy 0 repair 0 ITERATION 49:  destroy 0 repair 0 ITERATION 50:  ITERATION 51:  ITERATION 52:  destroy 4 repair 0 destroy 4 repair 3 ITERATION 53:  ITERATION 54:  destroy 0 repair 0 ITERATION 55:  ITERATION 56:  ITERATION 57:  ITERATION 58:  destroy 0 repair 0 ITERATION 59:  ITERATION 60:  destroy 0 repair 0 destroy 4 repair 0 destroy 4 repair 3 ITERATION 61:  ITERATION 62:  ITERATION 63:  destroy 4 repair 0 destroy 4 repair 3 ITERATION 64:  ITERATION 65:  ITERATION 66:  ITERATION 67:  destroy 0 repair 0 ITERATION 68:  destroy 4 repair 3 ITERATION 69:  ITERATION 70:  ITERATION 71:  destroy 4 repair 3 ITERATION 72:  ITERATION 73:  destroy 0 repair 0 ITERATION 74:  destroy 0 repair 0 destroy 0 repair 0 ITERATION 75:  ITERATION 76:  destroy 0 repair 0 destroy 0 repair 0 destroy 4 repair 0 destroy 4 repair 3 ITERATION 77:  ITERATION 78:  ITERATION 79:  ITERATION 80:  ITERATION 81:  destroy 0 repair 0 destroy 0 repair 0 destroy 4 repair 3 ITERATION 82:  destroy 4 repair 3 ITERATION 83:  destroy 4 repair 3 ITERATION 84:  ITERATION 85:  destroy 4 repair 3 ITERATION 86:  destroy 4 repair 0 destroy 4 repair 3 ITERATION 87:  destroy 4 repair 3 ITERATION 88:  ITERATION 89:  destroy 4 repair 0 destroy 4 repair 3ALNS iteration 89 is new global best, objective [117, 108, -20, 1761] BestDestroy4 BestRepair3
 ITERATION 90:  ITERATION 91:  destroy 4 repair 0 destroy 4 repair 3 ITERATION 92:  ITERATION 93:  ITERATION 94:  ITERATION 95:  destroy 4 repair 0 destroy 4 repair 3ALNS iteration 95 is new global best, objective [117, 108, -20, 1743] BestDestroy4 BestRepair3
 ITERATION 96:  ITERATION 97:  ITERATION 98:  destroy 0 repair 0 ITERATION 99:  destroy 0 repair 0 ITERATION 100: 
'''

data = '''
ITERATION 1:  ITERATION 2:  destroy 2 repair 0 destroy 12 repair 0 destroy 0 repair 1 destroy 2 repair 2 ITERATION 3:  ITERATION 4:  ITERATION 5:  destroy 13 repair 1 ITERATION 6:  ITERATION 7:  destroy 13 repair 1 destroy 0 repair 1 destroy 2 repair 0 destroy 2 repair 2 ITERATION 8:  destroy 2 repair 0 destroy 2 repair 2 ITERATION 9:  destroy 10 repair 2 ITERATION 10: ALNS iteration 10 is new global best, objective [110, 70, -27, 1452] BestDestroy8 BestRepair1
 ITERATION 11: ALNS iteration 11 is new global best, objective [110, 69, -26, 1475] BestDestroy0 BestRepair1
 ITERATION 12:  ITERATION 13:  destroy 2 repair 0 destroy 2 repair 2 ITERATION 14:  ITERATION 15:  ITERATION 16:  ITERATION 17:  ITERATION 18:  destroy 2 repair 0 destroy 2 repair 2 ITERATION 19:  ITERATION 20:  ITERATION 21:  ITERATION 22:  destroy 13 repair 1 ITERATION 23:  ITERATION 24:  ITERATION 25:  ITERATION 26:  ITERATION 27:  ITERATION 28:  ITERATION 29:  destroy 0 repair 1 destroy 13 repair 1 ITERATION 30:  ITERATION 31:  ITERATION 32:  destroy 2 repair 0 destroy 2 repair 2 ITERATION 33:  destroy 13 repair 1 ITERATION 34:  ITERATION 35:  ITERATION 36:  ITERATION 37:  ITERATION 38:  destroy 13 repair 1 ITERATION 39:  destroy 8 repair 1ALNS iteration 39 is new global best, objective [113, 72, -23, 1837] BestDestroy8 BestRepair1
 ITERATION 40:  ITERATION 41:  destroy 2 repair 0 destroy 2 repair 2 ITERATION 42:  ITERATION 43:  destroy 12 repair 0 ITERATION 44:  destroy 10 repair 2 ITERATION 45:  ITERATION 46:  ITERATION 47:  ITERATION 48:  ITERATION 49:  ITERATION 50:  ITERATION 51:  ITERATION 52:  destroy 10 repair 3 destroy 10 repair 2 ITERATION 53:  ITERATION 54:  destroy 0 repair 1 ITERATION 55:  destroy 2 repair 0 ITERATION 56:  destroy 10 repair 3 destroy 10 repair 2 ITERATION 57:  ITERATION 58:  ITERATION 59:  ITERATION 60:  ITERATION 61:  destroy 2 repair 0 destroy 13 repair 1 destroy 2 repair 2 ITERATION 62:  destroy 0 repair 1 ITERATION 63:  ITERATION 64:  destroy 0 repair 1 ITERATION 65:  destroy 0 repair 1 destroy 12 repair 0 destroy 8 repair 1 ITERATION 66:  destroy 8 repair 1 ITERATION 67:  destroy 8 repair 1 destroy 13 repair 1 ITERATION 68:  ITERATION 69:  ITERATION 70:  destroy 13 repair 1 ITERATION 71:  destroy 2 repair 0 destroy 2 repair 2 ITERATION 72:  ITERATION 73:  destroy 0 repair 1 ITERATION 74:  destroy 12 repair 0 ITERATION 75:  ITERATION 76:  ITERATION 77:  ITERATION 78:  ITERATION 79:  destroy 12 repair 0 destroy 2 repair 0 destroy 13 repair 1 destroy 8 repair 1 destroy 10 repair 3 destroy 2 repair 2 ITERATION 80:  destroy 8 repair 1 ITERATION 81:  ITERATION 82:  destroy 8 repair 1 ITERATION 83:  destroy 2 repair 2 destroy 10 repair 2 ITERATION 84:  destroy 8 repair 1 ITERATION 85:  ITERATION 86:  destroy 12 repair 0 destroy 8 repair 1 destroy 10 repair 3 destroy 10 repair 2 ITERATION 87:  destroy 8 repair 1 destroy 10 repair 3 destroy 10 repair 2 ITERATION 88:  destroy 0 repair 1 ITERATION 89:  ITERATION 90:  destroy 10 repair 3 destroy 10 repair 2ALNS iteration 90 is new global best, objective [114, 78, -23, 1734] BestDestroy10 BestRepair3
 ITERATION 91:  ITERATION 92:  destroy 13 repair 1 ITERATION 93:  ITERATION 94:  destroy 10 repair 3 destroy 10 repair 2 ITERATION 95:  destroy 10 repair 2ALNS iteration 95 is new global best, objective [117, 75, -31, 1583] BestDestroy10 BestRepair2
 ITERATION 96:  ITERATION 97:  destroy 2 repair 0 destroy 13 repair 1 destroy 10 repair 3 destroy 2 repair 2 ITERATION 98:  ITERATION 99:  destroy 13 repair 1 ITERATION 100:  destroy 13 repair 1
'''
destroy_numbers = []
repair_numbers = []
dest_numbers = []
rep_numbers = []

import re

destroy_matches = re.findall(r'destroy (\d+)', data)
repair_matches = re.findall(r'repair (\d+)', data)
dest_matches = re.findall(r'BestDestroy(\d+)', data)
rep_matches = re.findall(r'BestRepair(\d+)', data)

destroy_numbers = [int(num) for num in destroy_matches]
repair_numbers = [int(num) for num in repair_matches]
dest_numbers = [int(num) for num in dest_matches]
rep_numbers = [int(num) for num in rep_matches]

# Count the occurrences
destroy_counter = Counter(destroy_numbers)
repair_counter = Counter(repair_numbers)
dest_counter = Counter(dest_numbers)
rep_counter = Counter(rep_numbers)

print("Destroy counts:", destroy_counter)
print("Repair counts:", repair_counter)
print("Dest counts:", dest_counter)
print("Rep counts:", rep_counter)

all_destroy_keys = set(destroy_counter.keys()) | set(dest_counter.keys())
min_destroy_key = min(all_destroy_keys)
max_destroy_key = max(all_destroy_keys)

# Find the range of keys for repair and rep
all_repair_keys = set(repair_counter.keys()) | set(rep_counter.keys())
min_repair_key = min(all_repair_keys)
max_repair_key = max(all_repair_keys)

# Print the values in ascending order by key for destroy and dest
print("Destroy counts:")
for key in range(0, max_destroy_key + 1):
    print(destroy_counter.get(key, 0))

print("\nDest counts:")
for key in range(0, max_destroy_key + 1):
    print(dest_counter.get(key, 0))

# Print the values in ascending order by key for repair and rep
print("\nRepair counts:")
for key in range(0, max_repair_key + 1):
    print(repair_counter.get(key, 0))

print("\nRep counts:")
for key in range(0,  max_repair_key + 1):
    print(rep_counter.get(key, 0))