<script>


const hello = 'hello world!';

console.log(hello);

class expando{
  get(target, name) {
    return `Value for attribute ${target} ${name}`
  }
}

let handler = {
  apply(target, name, data){
    return target._name+"/"+name+"!!!!!!!!!!!!!!!!!!!!!!!"
    console.log("@@@@@@@@@@@@@@",target,name,data)
    target[name] = data
     console.log("@@@ apply",target)

    return target
    
  },
  set(target, name, data){
    console.log("!!!",target,name,data)
    let spc = {"_value":1,"_name":1,"toJSON":1,"nodeType":1,"id":1,"className":1
                 ,"nodeName":1,"parentNode":1,"currentStyle":1,"outerHTML":1, 
                "window":1,"length":1}
    if (name in spc)
    {
      return Reflect.set(target, name, data)
    }
    else
    {
      	if (name in target){
        	target[name]._value = data
        	return target[name]._value
           return target[name]
           return Reflect.set(target, name, data)
        }
        else
        {
    		target[name] = exp(target._name+"/"+name,data,parent=target)
        	return target[name]._value
        }    
    }
   
     console.log("@@@ set",target)

    return target[name]
    
  },
  get(target, name, reciever) {
    
    if (typeof target[name] === 'function') {
      //return target[name].bind(target);
      return target[name];

    }

    
    if (name in target){
      if (target[name] != null && typeof target[name]._value === 'function') {
        //return target[name]._value.bind(target);
        //return target[name]._value;

      }
      return target[name]
    }
    
    //return Reflect.get(...arguments);
    // console.log("..........2....",name)
    let spc = {"_value":1,"_name":1,"toJSON":1,"nodeType":1,"id":1,"className":1
               ,"nodeName":1,"parentNode":1,"currentStyle":1,"outerHTML":1, 
              "window":1,"length":1}
    if (name in spc)
    {
       return Reflect.get(target, name, reciever)
    }
    else{ target[name] = exp(target._name+"/"+name,null,parent=target)
        }
  
    
    return target[name]
    return `Value for attribute ${target} ${name}`
  },
  
}

function exp(_name = "", value=null, parent = null){
  	let payload = {"_name":_name}
  	if (value != null){
      payload["_value"]=value
    }
	let x = new Proxy({"_name":_name,"_parent":parent, "_value":value}, handler);
	//x._name = name;
	return x
}

let xo = exp("namespace", "Awesome!")
console.log('.......')
// let x = new Proxy({}, expando);
console.log(xo); // produces message: "Value of attribute 'lskdjoau'"

// console.log(x.lskdjoau); // produces message: "Value of attribute 'lskdjoau'"
xo.a.b.c.d.e.f.g.h = 3
xo.a.b.c.d.e = () => {return "EEEEEEEEEEEEEEEEEEE"}
xo.a.b.c = () => {return "CCCCCCCCCCCCC"}

console.log(xo); // produces message: "Value of attribute 'lskdjoau'"
console.log(xo._name); // produces message: "Value of attribute 'lskdjoau'"
console.log(xo.a.b.c._value()); // produces message: "Value of attribute 'lskdjoau'"
console.log(xo.a.b.c.d.e._value()); // produces message: "Value of attribute 'lskdjoau'"
console.log(xo.a.b.c.d.e.f.g.h._value); // produces message: "Value of attribute 'lskdjoau'"










// ####################################################
// ####################################################
// ####################################################
// ####################################################

import io from 'socket.io-client';
	//   import { Server } from 'socket.io';
	export let name = "xo-svelte";
	export let change_count = 0;
	export let input_count = 0;

  let socket = io('http://127.0.0.1:5000');
  socket.on('server_update', msg => {
		console.log("::::::::::::::::::::::::::::: new message, msg: ", msg)
		message = msg.data;
    });
  let message = '-------------';

// socketIoHandler.js

export function onChanges(messagex) {
	input_count += 1
	console.log(":::::::::::::::::::::::::::::")
	socket.emit('user_msg', message);
	console.log(":::::::::::::::::::::::::::::")
}
export function sendSocketIOMessage(message) {
	console.log(":::::::::::::::::::::::::::::")
	socket.emit('user_msg', message);
	console.log(":::::::::::::::::::::::::::::")
}
// export function injectSocketIO(server) {
	
//     socket.on('new message', msg => {
// 		console.log("::::::::::::::::::::::::::::: new message, msg: ", msg)
// 		message = msg;
//     });
	
	// const io = new Server(server);
    // io.on('connection', (socket) => {
    //     let username = `User ${Math.round(Math.random() * 999999)}`;
    //     socket.emit('name', username);

    //     socket.on('message', (message) => {
    //         io.emit('message', {
    //             from: username,
    //             message: message,
    //             time: new Date().toLocaleString()
    //         });
    //     });
    // });

//     console.log('SocketIO injected');
// }
//   onMount(async () => {
//     socket = io('http://127.0.0.1:5000');

//     socket.on('new message', msg => {
//       message = msg;
//     });
//   });
</script>



<main>
	<h1>Hello {name}!</h1>
		
		<input bind:value={message} 
		placeholder="Enter a message"
		on:change={() => change_count += 1}
		on:input={() => onChanges(message)} 		
		/>
		
		<button on:click={() => sendSocketIOMessage(message)}>
			Send message
		</button>
		
	<!-- <input bind:value={message} placeholder="Enter a message" on:change={() => change_count += 1}
	on:input={() => onChanges(message)} />
		<button on:click={() => sendSocketIOMessage(message)}>
			Send message
		</button> -->
		
	<p>{message}</p>
	<p>{change_count}</p>
	<p>{input_count}</p>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>