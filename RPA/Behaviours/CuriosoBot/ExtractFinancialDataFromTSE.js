const CuriosoBot = require('../../Bots/CuriosoBot')

const Curioso = new CuriosoBot('https://divulgacandcontas.tse.jus.br/divulga/#/estados/2018/2022802018/BR/candidatos')
Curioso.openCandidatesListURI('https://divulgacandcontas.tse.jus.br/divulga/#/estados/2018/2022802018/BR/candidatos')
Curioso.getCandidatesTable().then((r)=>{

    r.forEach(element => {
        console.log(element)
    });
    Curioso.end()
}).catch((e)=>{
    console.log(e)
    Curioso.end()
})
