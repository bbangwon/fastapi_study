<script>
  import fastapi from "../lib/api";
  let question_list = [];

  async function get_question_list() {
    try{
      const data = await fastapi('get', '/api/question/list');
      question_list = data;
    }
    catch (error) {
      console.error('Error fetching question list:', error);
    }
  }

  get_question_list();

</script>

<ul>
  {#each question_list as question}
    <li>{question.subject}</li>
  {/each}
</ul>