import gradio as gr

def greet(name, intensity):
    return "Hola amigo, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict"
)

demo.launch(share=True)