<script>
  import fastapi from "../lib/api";
  import { link } from "svelte-spa-router";
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
    <li><a use:link href="/detail/{question.id}">{question.subject}</a></li>
  {/each}
</ul>