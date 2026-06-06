Planning Specification The Unofficial Off-Campus Housing Guide
Domain
Summary Define your domain (e.g., student off-campus housing). Briefly explain why this information is valuable (e.g., helps students avoid predatory leases, illegal room occupancy fines) and why it is hard to find through official university websites alone (e.g., fragmented data, complex municipal ordinances).

Documents
List your 10+ source PDFs here, including the local file paths (e.g., CUsersParthDesktopCodePathai201_RAG_p1housing_pdf_ingest_pdfname.pdf). Aim for a mix of university handbooks and municipal guides.

Chunking Strategy
Chunk Size 750 characters

Chunk Overlap 75 characters

Reasoning Since these housing guides contain a mix of structured lists (rules, fines) and dense legal prose (lease rights), 750 characters is small enough to ensure a specific rule fits into one chunk but large enough to retain context for complex policies. The 10% overlap (75 characters) ensures that if a key sentence is split, the semantic meaning is preserved in both chunks.

Retrieval Approach
Embedding Model all-MiniLM-L6-v2 (via sentence-transformers, running locally).

Retrieval Count (Top-k) 4 chunks.

Trade-offs While this local model is fast and free, it may struggle with highly specialized legal terminology or international languages. In a production system, I would consider moving to a commercial API model (e.g., OpenAI or Cohere) for better accuracy on domain-specific text and improved support for non-English queries.

Architecture
Code snippet
graph TD
    A[PDF Source Files] --pdfplumber Text Extraction B[Raw Markdown Text Data]
    B --750 Char Splitter  75 Overlap C[Document Text Chunks]
    C --all-MiniLM-L6-v2 Model D[Vector Embeddings]
    D --Persistent Local Storage E[(ChromaDB Vector Store)]
    F[User Plain-Language Query] --Semantic Match Optimization E
    E --Retrieve Top-k=4 Context Chunks G[Grounded Context Prompt]
    F -- G
    G --Llama-3.3-70b-Versatile H[LLM Generation Engine]
    H --Cited Grounded Output I[Gradio Web UI Interface]

Evaluation Plan
Question What is the recommended move-in checklist for off-campus housing according to the University of New Haven guide

Expected Answer Take pictures of the apartment, complete a written inventory signed by the landlord, move in with roommates, park legally, keep doors locked, bring cleaning supplies, and unpack one room at a time.

Question According to the University of Delaware off-campus guide, what are the specific consequences if a lease automatically renews

Expected Answer If 60-day notice isn't given, the lease may continue month-to-month or automatically renew for another full year if the tenant fails to vacate or reject new terms in writing.

Question What are the consequences for a minor possessing alcohol or driving a vehicle with alcohol inside in Connecticut

Expected Answer Minors can be fined $200–$500; driver's license suspension up to 150 days (or 60 days if found inside a vehicle they are driving).

Question What specific household cooking appliances are explicitly prohibited in student residential spaces according to the PennWest Clarion handbook

Expected Answer Air fryers, crockpots, deep fryers, electric skillets, hot plates, instant pots, sous vide immersion cookers, indooroutdoor grills, pressure cookers, rice cookers, sandwich makers, toasters, toaster ovens, waffle makers, and non-air popper popcorn makers.

Question Under what conditions can a landlord enter a rented property without 48 hours notice according to the Delaware Landlord-Tenant Code

Expected Answer Only for emergencies or for repairs specifically requested by the tenant.

Anticipated Challenges
Formatting Heterogeneity Distinguishing between headings, body text, and tables within PDFs can lead to fragmented chunks.

Attribution Errors Multiple documents might contain the same Good Neighbor policies; the system must correctly attribute each chunk to its source file to avoid confusing the user about which state laws apply.

AI Tool Plan
IngestionChunking I will provide the Chunking Strategy section to the AI to generate a robust ingest.py script that uses pdfplumber to extract and clean text.

RetrievalInterface I will use the AI to wire the ChromaDB retrieval logic and ensure the Gradio UI accurately displays source attribution for every answer.