from flask import Flask,render_template
import random,time,sys,datetime

app = Flask(__name__)

def create_lucky(seed):
	LUCKY_SEED=int(seed)
	redball=list(range(1,36))
	blueball=list(range(1,13))
	redball_left=35
	blueball_left=12
	lucky_ball=0
	redball_pool=[]
	blueball_pool=[]
	random.shuffle(redball)
	random.shuffle(blueball)
	for i in range(5):
		time.sleep(random.randint(1,LUCKY_SEED)/LUCKY_SEED)
		for j in range(random.randint(1,LUCKY_SEED)%redball_left):
			random.shuffle(redball)
		lucky_ball=redball.pop()
		# print("LUCKY_BALL is %s" %(lucky_ball))
		redball_pool.append(lucky_ball)
		redball_left=redball_left-1
	# print("BLUE BALL IS ROLLING")
	for i in range(2):
		time.sleep(random.randint(1,LUCKY_SEED)/LUCKY_SEED)
		for j in range(random.randint(1,LUCKY_SEED)%blueball_left):
			# print(blueball)
			random.shuffle(blueball)
		# print(blueball)
		lucky_ball=blueball.pop()
		# print("LUCKY_BALL is %s" %(lucky_ball))
		blueball_pool.append(lucky_ball)
		blueball_left=blueball_left-1
	redball_pool.sort()	
	blueball_pool.sort()
	# lottery=str(redball_pool+blueball_pool).replace('[','').replace(']','\n')
	redball_pool.extend(blueball_pool)
	return redball_pool

def create_dantuo(seed):
	LUCKY_SEED=int(seed)
	redball=list(range(1,36))
	blueball=list(range(1,13))
	redball_left=35
	blueball_left=12
	lucky_ball=0
	redballdan_pool=[]
	redballtuo_pool=[]
	blueballdan_pool=[]
	blueballtuo_pool=[]
	random.shuffle(redball)
	random.shuffle(blueball)
	for i in range(4):
		time.sleep(random.randint(1,LUCKY_SEED)/LUCKY_SEED)
		for j in range(random.randint(1,LUCKY_SEED)%redball_left):
			random.shuffle(redball)
		lucky_ball=redball.pop()
		# print("LUCKY_BALL is %s" %(lucky_ball))
		redballdan_pool.append(lucky_ball)
		redball_left=redball_left-1
	for i in range(7):
		time.sleep(random.randint(1,LUCKY_SEED)/LUCKY_SEED)
		for j in range(random.randint(1,LUCKY_SEED)%redball_left):
			random.shuffle(redball)
		lucky_ball=redball.pop()
		# print("LUCKY_BALL is %s" %(lucky_ball))
		redballtuo_pool.append(lucky_ball)
		redball_left=redball_left-1
	# print("BLUE BALL IS ROLLING")
	for i in range(1):
		time.sleep(random.randint(1,LUCKY_SEED)/LUCKY_SEED)
		for j in range(random.randint(1,LUCKY_SEED)%blueball_left):
			# print(blueball)
			random.shuffle(blueball)
		# print(blueball)
		lucky_ball=blueball.pop()
		# print("LUCKY_BALL is %s" %(lucky_ball))
		blueballdan_pool.append(lucky_ball)
		blueball_left=blueball_left-1
	for i in range(2):
		time.sleep(random.randint(1,LUCKY_SEED)/LUCKY_SEED)
		for j in range(random.randint(1,LUCKY_SEED)%blueball_left):
			# print(blueball)
			random.shuffle(blueball)
		# print(blueball)
		lucky_ball=blueball.pop()
		# print("LUCKY_BALL is %s" %(lucky_ball))
		blueballtuo_pool.append(lucky_ball)
		blueball_left=blueball_left-1
	redballdan_pool.sort()	
	redballtuo_pool.sort()	
	blueballdan_pool.sort()
	blueballtuo_pool.sort()
	lottery=str(redballdan_pool)+'+'+str(redballtuo_pool)+'    '+str(blueballdan_pool)+'+'+str(blueballtuo_pool)
	return lottery

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/8888/')
@app.route('/8888/<name>')
def single(name=None):
    return render_template('hello.html', name=create_lucky(name))
@app.route('/8848/')
@app.route('/8848/<name>')
def dantuo(name=None):
    return render_template('more.html', name=create_dantuo(name))