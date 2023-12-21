
import pprint
import google.generativeai as palm

import json

API_KEY = "AIzaSyD6Vejra_NrillERrQnP8VpCOSNR8ruvZs"

palm.configure(api_key=API_KEY)

model = "models/text-bison-001"




# 
def prompt_function(prompt_word,chat_prompt):
    prompt = f"""
    Consider yourself as a expert in extracting details from a given text,
    {
        chat_prompt
    }
    From the above prompt find the {prompt_word} and strictly return the {prompt_word} alone"""
    return prompt



def rasa_text_extract_company_name(chat_prompt):

    completion = palm.generate_text(
        model=model,
        prompt=prompt_function("company name", chat_prompt),
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )

    company_name = completion.result

    # print(company_name)

    slot_data = {}

    slot_data["company_name"] = company_name

    print(slot_data)

    return slot_data

def rasa_text_extract_company_name_project_name(chat_prompt):

    completion = palm.generate_text(
        model=model,
        prompt=prompt_function("company name", chat_prompt),
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )

    company_name = completion.result

    # project name

    completion = palm.generate_text(
        model=model,
        prompt=prompt_function("project name", chat_prompt),
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )

    project_name = completion.result

    # print(company_name)
    # print(project_name)

    slot_data = {}

    slot_data["company_name"] = company_name
    slot_data["project_name"] = project_name

    print(slot_data)

    return slot_data



def rasa_text_extract_all_three(chat_prompt):

    # print("im inside rasa text extract")

    # prompt = f"""
    # Consider yourself as a expert in extracting details from a given text,

    # {
    #     chat_prompt
    # }

    # From the above prompt find the company name, project name, document type, return None if any of the parameter is not present in the above prompt

    # add the data and return the ouptut in the below mentioned format

    # {{
    # "compnay_name": 'name of the company',
    # "project_name": 'name of the project',
    # "doc_type": 'type of the document'
    # }}


    # """

    # completion = palm.generate_text(
    #     model=model,
    #     prompt=prompt,
    #     temperature=0,
    #     # The maximum length of the response
    #     max_output_tokens=800,
    # )

    # # print(completion.result)


    # op = completion.result

    # start_index = op.find('{')
    # end_index = op.rfind('}') + 1
    
    # # Extract the substring containing the JSON content
    # json_content_str = op[start_index:end_index].strip()

    # print(json_content_str)

    
    
    # # Print the extracted JSON content
    # # print(json_content_str)


    # # Convert dictionary to JSON string
    # output_json = "dad"


    # print(output_json)


    completion = palm.generate_text(
        model=model,
        prompt=prompt_function("company name", chat_prompt),
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )

    company_name = completion.result

    # project name

    completion = palm.generate_text(
        model=model,
        prompt=prompt_function("project name", chat_prompt),
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )

    project_name = completion.result

    # document type

    completion = palm.generate_text(
        model=model,
        prompt=prompt_function("document type", chat_prompt),
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )

    doc_type = completion.result


    # print(company_name)
    # print(project_name)
    # print(doc_type)

    slot_data = {}

    slot_data["company_name"] = company_name
    slot_data["project_name"] = project_name
    slot_data["doc_type"] = doc_type

    print(slot_data)


    return slot_data











