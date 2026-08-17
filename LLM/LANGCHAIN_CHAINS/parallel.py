import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"))

llm1 = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"))


model1 = ChatHuggingFace(llm=llm)
model2=ChatHuggingFace(llm=llm1)
parser=StrOutputParser()

prompt1=PromptTemplate(
    template='Give small and simple texts for the following text \n {text}',
    input_variables=['text']
)
prompt2=PromptTemplate(
    template='Genarate 5 short question answers from the following texts \n{text}',
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template='Merge the provided notes into a single document.\n\n'
             'Notes:\n{notes}\n\n'
             'Quiz:\n{quiz}',
    input_variables=['notes', 'quiz']
)


parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {'notes':prompt1 | model1 | parser,
    'quiz':prompt2 | model1 | parser
    })

merge_chain = prompt3 | model1 | parser
chain = parallel_chain | merge_chain
text="""" Recurrent Neural Networks (RNNs) are a class of neural networks designed to process sequential data by retaining information from previous steps. They are especially effective for tasks where context and order matter.

Designed for sequential and temporal data
Maintains memory of past inputs
Widely used in NLP, forecasting and speech tasks
introduction_to_recurrent_neural_network.webpintroduction_to_recurrent_neural_network.webp
Imagine reading a sentence and you try to predict the next word, you don’t rely only on the current word but also remember the words that came before. RNNs work similarly by “remembering” past information i.e it considers all the earlier words to choose the most likely next word.

This memory of previous steps helps the network understand context and make better predictions.
Recurrent Neural Network Architecture
RNNs share similarities in input and output structures with other deep learning architectures but differ significantly in how information flows from input to output. Unlike traditional deep neural networks where each dense layer has distinct weight matrices. RNNs use shared 
Working of RNN
At each time step RNNs process units with a fixed activation function. These units have an internal hidden state that acts as memory that retains information from previous time steps. This memory allows the network to store past knowledge and adapt based on new inputs.

Updating the Hidden State in RNNs
The current hidden state 
1. Simplified Gradient Calculation:
  

2. Handling Dependencies in Layers: Each hidden state is updated based on its dependencies:

The gradient is then calculated for each state, considering dependencies from previous hidden states.

3. Gradient Calculation with Explicit and Implicit Parts: The gradient is broken down into explicit and implicit parts summing up the indirect paths from each hidden state to the weights.
 

4. Final Gradient Expression: The final derivative of the loss function with respect to the weight matrix W is computed:

This iterative process is the essence of backpropagation through time.

Types Of Recurrent Neural Networks
There are four types of RNNs based on the number of inputs and outputs in the network:

1. One-to-One RNN
This is the simplest type of neural network architecture where there is a single input and a single output. It is used for straightforward classification tasks such as binary classification where no sequential data is involved.

one_to_one
One-to-One RNN
2. One-to-Many RNN
In a One-to-Many RNN the network processes a single input to produce multiple outputs over time. This is useful in tasks where one input triggers a sequence of predictions (outputs). For example in image captioning a single image can be used as input to generate a sequence of words as a caption.

multiple_outputs
One-to-Many RNN
3. Many-to-One RNN
The Many-to-One RNN receives a sequence of inputs and generates a single output. This type is useful when the overall context of the input sequence is needed to make one prediction. In sentiment analysis the model receives a sequence of words (like a sentence) and produces a single output like positive, negative or neutral.

multiple_inputs
Many-to-One RNN
4. Many-to-Many RNN
The Many-to-Many RNN type processes a sequence of inputs and generates a sequence of outputs. In language translation task a sequence of words in one language is given as input and a corresponding sequence in another language is generated as output."""

result=chain.invoke({'text':text})
print(result)

chain.get_graph().print_ascii()