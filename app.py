import gradio as gr
from generate import ask

def handle_query(question):
    result = ask(question)
    sources = "\n".join(f"• {s}" for s in result["sources"])
    return result["answer"], sources

with gr.Blocks(title="Campus Housing RAG Explorer") as demo:
    gr.Markdown("# Education Institution Housing Guide Search Engine")
    gr.Markdown("Query the cross-university database")
    
    with gr.Row():
        with gr.Column():
            inp = gr.Textbox(label="Enter Housing Policy Inquiry", placeholder="e.g., What is the policy for off-campus guests?")
            btn = gr.Button("Search")
        with gr.Column():
            answer = gr.Textbox(label="Answer", lines=8, interactive=False)
            sources = gr.Textbox(label="Verified Source Manuals", lines=3, interactive=False)
            
    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

if __name__ == "__main__":
    demo.launch()