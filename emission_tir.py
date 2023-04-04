import InfraLib
import uui
import RPi.GPIO as GPIO

tankID = uui.getnode()


def IRBlast(tankID, projectile_type, verbose=False):
	if projectile_type == 'LASER':
		projectil_id = 0xF1
	else :
		if verbose:
			print('unknows')
		
		return False
	
	msg = (str(bin(projectile_id))[2:] + str(bin(tankID))[2:])
	
	if verbose :
		print("send :",msg)
	
	IR(23, 'NEC', dict()).send_code(encodeMsg(msg)+'0')
	return True
	
	
InfraLib.IRBlast(tankID,"LASER")
