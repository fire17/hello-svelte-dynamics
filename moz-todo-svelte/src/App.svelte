<script>
	  import io from 'socket.io-client';
	//   import { Server } from 'socket.io';
	export let name;
	export let input_count = 0;
	export let change_count = 0;

  let socket = io('http://127.0.0.1:5000');
  socket.on('new message', msg => {
		console.log("::::::::::::::::::::::::::::: new message, msg: ", msg)
		message = msg;
    });
  let message = '-------------';
// socketIoHandler.js

export function onChanges(messagex) {
	input_count += 1
	console.log(":::::::::::::::::::::::::::::")
	socket.emit('send message', message);
	console.log(":::::::::::::::::::::::::::::")
}
export function sendSocketIOMessage(message) {
	console.log(":::::::::::::::::::::::::::::")
	socket.emit('send message', message);
	console.log(":::::::::::::::::::::::::::::")
}
export function injectSocketIO(server) {
	
    socket.on('new message', msg => {
		console.log("::::::::::::::::::::::::::::: new message, msg: ", msg)
		message = msg;
    });
	
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

    console.log('SocketIO injected');
}
//   onMount(async () => {
//     socket = io('http://127.0.0.1:5000');

//     socket.on('new message', msg => {
//       message = msg;
//     });
//   });
</script>



<main>
	<h1>Hello {name}!</h1>
		
		<input bind:value={message} placeholder="Enter a message" on:change={() => change_count += 1}
	on:input={() => onChanges(message)} />
		<button on:click={() => sendSocketIOMessage(message)}>
			Send message
		</button>
		
	
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