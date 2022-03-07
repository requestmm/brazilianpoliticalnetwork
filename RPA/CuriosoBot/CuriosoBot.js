/**
 * CurisoBot.js or Curioso is the bot responsible to extract electoral data from electoral open sources.
 * 
 */
 const {spawn} = require('child_process');

 const CuriosoBotPython = spawn('pipenv run python CuriosoBot.py', {shell: true});

 CuriosoBotPython.stdout.on('data', (data)=>{
    console.log(data.toString())
 })
 