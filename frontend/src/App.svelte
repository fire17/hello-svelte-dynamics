<script>
  import io from 'socket.io-client';

  let socket;
  let message = '';

  onMount(async () => {
    socket = io('http://localhost:5000');

    socket.on('new message', msg => {
      message = msg;
    });
  });
</script>

<input bind:value={message} placeholder="Enter a message" />

<button on:click={() => socket.emit('send message', message)}>
  Send message
</button>

<p>{message}</p>
