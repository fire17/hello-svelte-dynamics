import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		// name: 'world'
		name: 'xo-svelte'
	}
});

export default app;