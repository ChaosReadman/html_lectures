# ���W���[���錾/�ϐ�������
use strict;
my %cf;
#��������������������������������������������������������������������
#�� Windy Chat : init.cgi - 2011/10/02
#�� Copyright(C) KentWeb
#�� http://www.kent-web.com/
#��������������������������������������������������������������������
$cf{version} = 'WindyChat v2.1';
#��������������������������������������������������������������������
#�� [���ӎ���]
#�� 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����
#��    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B
#�� 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B
#��    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B
#��������������������������������������������������������������������

#===========================================================
# �� ��{�ݒ�
#===========================================================

# �^�C�g����
$cf{chat_title} = "Chat Room";

# �ő�ۗL�L�����i����𒴂���L���͎����폜�����j
$cf{maxlog} = 30;

# �߂���URL (http://����L�q���Ă��悢)
$cf{homepage} = '../../simplebbs.html';

# �X�N���v�g�� (���̌f���̃t�@�C����)
$cf{chat_cgi} = "./windy.cgi";

# ���O�t�@�C���i�t���p�X�ŋL�q����ꍇ�� / ����n�܂�p�X�j
$cf{logfile} = "./data/log.cgi";

# �Q���҃t�@�C���i�t���p�X�ŋL�q����ꍇ�� / ����n�܂�p�X�j
$cf{memfile} = "./data/mem.cgi";

# �e���v���[�g�f�B���N�g���y�T�[�o�p�X�z
$cf{tmpldir} = './tmpl';

# �����F
# �� �����F�Ƃ��̖��O���R���}�ŋ�؂�
$cf{colors} = [
	'#0000FF,��',
	'#DF0000,��',
	'#008040,�݂ǂ�',
	'#800000,��',
	'#C100C1,��',
	'#FF80C0,�s���N',
	'#FF8040,�I�����W',
	'#000080,��',
	];

# ���ގ������b�Z�[�W
# �� ���ɁA�������A�ގ���
$cf{msg_in}  = "����A��������Ⴂ�B";
$cf{msg_out} = "����A���悤�Ȃ�`�B";

# ���ގ��ē��̔��M�Җ�
$cf{master_name} = "MASTER";

# ���ގ��ē����b�Z�[�W�̐F
$cf{master_color} = "#808080";

# �������̑O�ɂ��|�C���^
$cf{pointer} = '��';

# �ő�󗝃T�C�Y�i�o�C�g�j
$cf{maxdata} = 10240;

#===========================================================
# �� �ݒ芮��
#===========================================================

# �ݒ�l��Ԃ�
sub init {
	return %cf;
}


1;
