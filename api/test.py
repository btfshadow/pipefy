import requests
import json
import os
from dotenv import load_dotenv
import string
import random

load_dotenv()

token = os.getenv("BEARER_TOKEN")
class TestGroup:
  def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
      return ''.join(random.choice(chars) for _ in range(size))

  def test_create_pipe(self):
      """
      Test create a pipe and expect a return of id
      """
      query = """
        mutation {
          createPipe(input: $input) {
            pipe {
                id
            }
          }
        }
      """
      task_variables = {
          "input": {
              "organization_id": '300915844',
              "name": f"My Test Phase {self.id_generator()}"
          }
      }
      headers = {
          'Authorization': f'Bearer {token}'
      }
      response = requests.post('https://api.pipefy.com/graphql', json={'query': query, 'variables': task_variables}, headers=headers)
      data = json.loads(response.text)
      assert response.status_code == 200
      assert type(data['data']['createPipe']['pipe']['id']) is str
      
  def test_create_phase(self):
      """
      Test create a phase and return the ID.
      """
      query = """
        mutation {
          createPhase(input: { input: $input }) {
            phase {
              id
            }
          }
        }
      """
      headers = {
          'Authorization': f'Bearer {token}'
      }

      task_variables = {
          "input": {
              "pipe_id": '302980702',
              "name": f"My Test Phase {self.id_generator()}"
          }
      }

      response = requests.post('https://api.pipefy.com/graphql', json={'query': query, 'variables': task_variables}, headers=headers)
      data = json.loads(response.text)
      print(response)
      assert response.status_code == 200
      
      assert type(data['data']['createPhase']['phase']['id']) is str


  def test_create_card(self):
      """
      Test create a phase and return the ID.
      """
      query = """
      mutation {
        createCard(input: {
          pipe_id: 302980702,
          title: "New card",
          fields_attributes:[
            {field_id: "field_1", field_value: "Value 1"},
            {field_id: "field_2", field_value: "Value 2"}
          ]}
        ) {
          card {
            title
          }
        }
      }
      """
      headers = {
          'Authorization': f'Bearer {token}'
      }

      response = requests.post('https://api.pipefy.com/graphql', json={'query': query}, headers=headers)
      data = json.loads(response.text)
      print(response)
      assert response.status_code == 200
