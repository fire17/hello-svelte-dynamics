# hello-svelte-dynamics
Teaching myself (with the help of ChatGPT) to deploy a Python-Svelte App using socketio and 2-way binded data


# install dependencies
npm install --save-dev rollup rollup-plugin-node-resolve rollup-plugin-commonjs rollup-plugin-svelte rollup-plugin-terser sirv-cli svelte socket.io-client

python3 -m pip install -r requirements.txt

# start python server
python3 app.py

# start development server
npm run dev

# build for production and launch server
npm run build
npm start

# generate static project
npm run export

# deploy to github pages
npm run deploy

