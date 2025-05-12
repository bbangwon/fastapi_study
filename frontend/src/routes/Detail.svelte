<script>    
    import fastapi from "../lib/api";
    
    export let params = {};
    let question_id = params.question_id;
    
    let question = {};

    async function get_question() {
        question = await fastapi('get', '/api/question/detail/' + question_id)
    }

    get_question();
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
</div>