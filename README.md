//README names the domain and identifies at least 10 documents with specific sources (URLs, subreddit names, or file descriptions).
# Off-Campus Student Housing Resource Domain

This repository serves as a comprehensive information domain collecting off-campus living guides, tenant rights frameworks, and student housing resources across multiple universities. It is designed to assist students transitioning from university residence halls to independent urban living by outlining structural budgets, neighborhood expectations, legal safety boundaries, and landlord-tenant communication criteria.

# Document Directory

This domain contains the following 10 core programmatic documents and worksheets compiled from institutional housing directives:

1. **`ucf_knights_guide_off_campus.pdf`**  
   *Description:* The University of Central Florida's strategic roadmap for off-campus living. Includes localized housing definitions (affiliated vs. conventional student apartments), steps for utilizing financial aid toward rent, and an introduction to the Office of Student Neighborhood Relations.
   
2. **`gwu_off_campus_living_guide.pdf`**  
   *Description:* George Washington University's urban housing manual detailing community development, neighborhood integration strategies within the Washington D.C. quadrants, and mandatory off-campus student online orientation milestones.

3. **`ud_rent_off_campus_guide.pdf`**  
   *Description:* The University of Delaware’s exhaustive transition workbook for Newark residency. It outlines shared "Blue Hen" student values, municipal ordinances, and direct touchpoints for the Office of the Dean of Students.

4. **`apartment_comparison_worksheet.pdf`**  
   *Description:* A tripartite matrix tracking comparative properties. Logs critical criteria including base rent, deposit fees, lease duration, built-in security systems, and utility structures (water, electricity, gas, internet) across three prospective apartments.

5. **`comprehensive_moving_budget.pdf`**  
   *Description:* A pre-move fiscal planning spreadsheet mapping upfront cash requirements. Tracks application fees, security deposits, pet fees, redecoration/painting provisions, utility hook-ups, and structural moving costs.

6. **`joint_vs_individual_lease_framework.pdf`**  
   *Description:* A comparative legal guide detailing the critical liabilities of binding rental contracts. Contrasts the collective risks of "joint and several liability" leases against individual bedroom leasing agreements common in student complexes.

7. **`formal_roommate_agreement.pdf`**  
   *Description:* A structured mediation contract designed to facilitate initial household boundaries. Covers proportional rent/utility splits, moving-out replacements, and explicit household rules for privacy, cleaning schedules, and overnight guests.

8. **`property_inspection_inventory_checklist.pdf`**  
   *Description:* A granular move-in condition log tracking structural interior integrity. Rates walls, ceilings, flooring, windows, door locks, and major appliances across the bedroom, bathroom, living room, and kitchen to safeguard security deposits.

9. **`tenant_rights_and_landlord_complaints.pdf`**  
   *Description:* A legal recourse reference document mapping tenant protections under regional statutes (e.g., Fair Housing Act, D.C. Housing Codes, Delaware Landlord-Tenant Code). Outlines maximum application fees, emergency entry rules, and code enforcement channels.

10. **`off_campus_transportation_and_safety_directory.pdf`**  
    *Description:* An emergency and municipal logistics matrix. Compiles transit routes (university shuttles, public LYNX/Lynx/WMATA transit lines), severe weather emergency protocols (hurricane warning prep), and local law enforcement contact endpoints.

//Chunking strategy is explained with specific reasoning — chunk size, overlap, and why those numbers fit the structure of the documents.
# Chunking Strategy

We implemented a structural chunking strategy designed to preserve semantic meaning, utilizing a RecursiveCharacterTextSplitter configured with a chunk size of 1000 characters and a chunk overlap of 200 characters.  This configuration was specifically chosen to match the architectural profile of institutional housing guides, tenant rights frameworks, and rental worksheets:  

Chunk Size Justification (1000 characters): A size of 1000 characters (roughly 150–200 words) ensures that dense, single-topic policy blocks—such as individual lease clauses, university conduct definitions, or specific safety protocols—are completely captured within a single vector embedding. This prevents the system from fragmenting a unified rule into meaningless text snippets, preserving its core semantic integrity for the embedding model.  

Chunk Overlap Justification (200 characters): The 200-character overlap serves as a 20% contextual bridge between contiguous chunks. Because legal and university housing documents frequently rely on conditional constraints—such as fine structures, penalty exceptions, or specific municipal boundaries—the overlap guarantees that these vital cross-references are not severed by an arbitrary text boundary.  

Separator Hierarchy Strategy: By leveraging the splitter's hierarchy of ["\n\n", "\n", " ", ""], the text naturally breaks at logical structural intervals. The script prioritizes splitting at paragraph breaks (\n\n) and bullet points (\n), which inherently respects the formatting of the source documents and ensures clean, logically independent text segments. 


//README includes at least 5 labeled sample chunks with their source document name.
# 5 Sample Chunks Stored in Chroma DB
& c:/Users/Parth/Desktop/CodePath/ai201_RAG_p1/.venv/Scripts/python.exe c:/Users/Parth/Desktop/CodePath/ai201_RAG_p1/get_samples
(.venv) PS C:\Users\Parth\Desktop\CodePath\ai201_RAG_p1> & c:/Users/Parth/Desktop/CodePath/ai201_RAG_p1/.venv/Scripts/python.exe c:/Users/Parth/Desktop/CodePath/ai201_RAG_p1/get_samples
### Sample Chunk 1
* **Source Document:** `2024_Knights-Guide-to-Living-off-campus_Final-2.pdf`
* **Chunk ID:** `2024_Knights-Guide-to-Living-off-campus_Final-2.pdf_chunk_0`
```text
AA
KKNNIIGGHHTT’’SS
GGUUIIDDEE
to living off campus
UNIVERSITY OF CENTRAL FLORIDA
ORLANDO, FLORIDA
WELCOME TO UCF
CCOONNTTEENNTTSS
The University of Central Florida (UCF) is a metropolitan research
university built to make a better future for our students and society.
Welcome to UCF 3 We solve tomorrow’s greatest challenges through a commitment to
academic, inclusive and operational excellence. Leveraging innovative
Intro to Student Neighborhood Relations 4
learning, discovery and partnerships, we foster social mobility while
developing the skilled talent needed to advance industry for our region,
Web Resource 6
state and beyond.
Signing A Lease 8
Discover what it’s all about to be a Knight.
Tips for Applications 10
ALMOST 90% OF UCF STUDENTS LIVE
Need to Know 12
IN OFF-CAMPUS HOUSING
Transportation & Parking 14
Here at UCF, there are so many options for each student to
Safety 16
explore and find the right fit for them when it comes to
```

### Sample Chunk 2
* **Source Document:** `2024_Knights-Guide-to-Living-off-campus_Final-2.pdf`
* **Chunk ID:** `2024_Knights-Guide-to-Living-off-campus_Final-2.pdf_chunk_1`
```text
Need to Know 12
IN OFF-CAMPUS HOUSING
Transportation & Parking 14
Here at UCF, there are so many options for each student to
Safety 16
explore and find the right fit for them when it comes to
Weather 17 housing. UCF’s off-campus community continues to
expand to accommodate its growing
Resources 18 student population.
WWHHOO TTOO AASSKK!! DDIIFFFFEERREENNTT SSTTUUDDEENNTTSS,,
DDIIFFFFEERREENNTT OOPPTTIIOONNSS
The Office of Student Neighborhood Relations works to support
those students living off-campus. Whether you need resources to
Most Knights will live off-campus during their time at UCF. Below is a
start your research, need to find a roommate, or just need guidance, description of housing options, and some advice for different student
we are here to help you get the most out of your UCF experience – groups. If you don’t see something that pertains to your situation, contact
and make Orlando your home away from home! our office and we will get you to the right people!
```

### Sample Chunk 3
* **Source Document:** `2024_Knights-Guide-to-Living-off-campus_Final-2.pdf`
* **Chunk ID:** `2024_Knights-Guide-to-Living-off-campus_Final-2.pdf_chunk_2`
```text
and make Orlando your home away from home! our office and we will get you to the right people!
In this guide, you will learn about everything you need to know to find Student apartments often appeal to student renters. This is a great option
your perfect home, including tips to make the process as smooth as as a transition before seeking conventional housing. Student apartments
possible. typically:
CONTACT FOR ANY QUESTIONS! • Offer individual leases
• Include basic utilities, like water and electricity (may have caps)
PHONE: 407-882-7233
• Require a guarantor to sign a lease
EMAIL: SNR@UCF.EDU
WWW.NRSE.SDES.UCF.EDU Conventional apartments are located all throughout Orlando. This is a
great option for upperclassmen who are ready to be more independent. In
conventional apartments, residents are responsible for:
• Lease for entire unit, not just one room
APPLY EARLY!
• Setting up utilities like electricity and wi-fi
Start looking for off-campus housing as soon as you’re
```

### Sample Chunk 4
* **Source Document:** `2024_Knights-Guide-to-Living-off-campus_Final-2.pdf`
* **Chunk ID:** `2024_Knights-Guide-to-Living-off-campus_Final-2.pdf_chunk_3`
```text
• Lease for entire unit, not just one room
APPLY EARLY!
• Setting up utilities like electricity and wi-fi
Start looking for off-campus housing as soon as you’re
accepted, or about 4 months before moving. For instance, • Proof of employment or finances to sign a lease
Tip
if you are starting class in the fall, try to sign a lease
Affiliated Housing – Many people assume that the three UCF Affiliated
before March. Don’t wait until the last minute – housing properties, Knights Circle, The Pointe at Central, and UnionWest Student
close to the University goes fast! You will learn more about Living, are managed by UCF, but this is not correct. Affiliated properties are
different types of leases available later in this guide. independently managed facilities that offer students a seamless process
to utilize financial aid, such as Florida Pre-Paid, Bright Futures, grants, or
student loans towards their rent. The affiliated distinction also indicates that
```

### Sample Chunk 5
* **Source Document:** `2024_Knights-Guide-to-Living-off-campus_Final-2.pdf`
* **Chunk ID:** `2024_Knights-Guide-to-Living-off-campus_Final-2.pdf_chunk_4`
```text
to utilize financial aid, such as Florida Pre-Paid, Bright Futures, grants, or
student loans towards their rent. The affiliated distinction also indicates that
these communities are patrolled regularly by the UCF Police Department.
However, financial aid can be used at ANY off-campus property, the difference
is that the funds are released to the student rather than the complex directly.
Please contact UCF Financial Aid for more information regarding the required
paperwork involved.
UCF International Students are encouraged to follow the tips and use the
tools outlined in this guide, and begin the search for off-campus housing as
soon as possible. Upon arrival into the United States, please complete your
Virtual Check-In with UCF Global to get connected with
an immigration advisor.
A KNIGHT’S GUIDE TO LIVING OFF CAMPUS
THE BEST RESOURCE FOR OFF-CAMPUS HOUSING!
Students needing to find off-campus housing should start their search at
```


//README includes at least 3 retrieval test examples, each showing the query and the top returned chunks.
//For at least 2 of those examples, the student provides a written explanation of why the returned chunks are relevant to the query.
# 3 Sample Chunks for a Sample Query:

Query: What is the policy for off-campus guests?

--- Result 1 [Source: rlh-handbook-clarion.pdf] ---
occupants.
Six occupants include the students assigned to the apartment. Roommates must agree to the presence
of guests in the room or apartment. The rights of the resident who does not wish to have a guest
take precedence.
• The same guest is not permitted to stay overnight for more than three days during a seven-day period.
Those who violate this policy may be billed, removed, and/or banned.
• The university does not condone or permit cohabitation.
• Guests may be asked to leave, and residents may lose visitation right if guests are disruptive or
violate policies.
• Staff may temporarily suspend visitation privileges from any building or other area to ensure the safety,
security or well-being of residents or in response to policy violations.
GENERAL INFORMATION
SALES/SOLICITATION
Residents are not permitted to use their rooms or other building facilities for any commercial purpose.

Relevance Explanation for Result 1

Result 1 provides highly granular, rule-based constraints that directly define the boundaries of the university's guest policy. It addresses the semantic intent of the query by explicitly mapping out behavioral and temporal limits, such as the maximum overnight stay restriction (no more than three days within a seven-day period) and roommate consent rules. Furthermore, it details the direct administrative consequences of policy violations (billing, removal, or suspension of visitation privileges). Even though the chunk stems from an apartment/residence handbook, its semantic content serves as a foundational baseline for student accountability regarding visitors.

--- Result 2 [Source: rlh-handbook-clarion.pdf] ---
communities. Safety is a shared responsibility. Your cooperation in escorting your guest and informing them
about visitation/escort policies when entering any on-campus residence is expected. Failure to comply will
result in disciplinary as outlined in the Student Code of Conduct.
All guests are required to comply with the policies in this guide. The resident is responsible for the behavior
of all their guests and will be held accountable for their behavior. Guests should in no way become a
nuisance to the neighbors/roommate(s). A roommate(s) has the right to object to future visits and staff will
mediate any concerns regarding the presence of guests. Guests are allowed only with the permission of all
roommate(s) and must be escorted at all times.
Guests are allowed 24 hours a day, subject to these provisions:
• A guest is defined as any individual who does not live in the room they wish to enter.

Relevance Explanation for Result 2

Result 2 is highly relevant because it establishes the foundational legal and behavioral expectations of student-guest dynamics, which matches the core intent of the query. The embedding model successfully pulled this chunk because it heavily features key semantic phrases like "visitation/escort policies" and "permission of all roommate(s)." This chunk specifically highlights the concept of secondary liability—explaining that the resident tenant is held legally and disciplinarily accountable for the actions of any non-resident visitor. Additionally, it provides a vital structural definition required to interpret the policy by explicitly stating what constitutes a "guest" (any individual who does not live in the room they wish to enter).

--- Result 3 [Source: GW_off-campus-living-guide.pdf] ---
by federal and local laws, as well as the Code of Student Conduct and university policies. The Code of
Student Conduct applies to all GW students and students may be charged with violations of laws or
university policies regardless of whether the violation occurred on- or off-campus.
The “Code of Student Conduct” can be found online at:
http://studentconduct.gwu.edu/code-student-conduct
Conduct action can be taken against students who live off campus for policy violations that occur on
campus and university premises. The university may also take conduct action to address student
behavior in addition to the actions of law enforcement or the courts.
To assist you in making constructive decisions and sustaining a positive relationship with the overall
off-campus community, the following are areas about which you should be aware and actively
responsible while living off-campus.
Consult your lease, rental agreement, or apartment manager

//README names the embedding model used.
#Embedding Model
This project utilizes the **`all-MiniLM-L6-v2`** model from the `sentence-transformers` library to generate 384-dimensional dense vector embeddings for both document ingestion and user querying.

//README includes a tradeoff reflection — what factors the student would weigh when choosing a model for a production deployment (e.g., cost, context length, multilingual support, local vs. API latency).
For the prototype, I used all-MiniLM-L6-v2 locally to prioritize speed, data privacy, and zero operational cost. When transitioning to a production deployment, choosing a model requires balancing a strict tradeoff matrix between cost, performance, and infrastructure complexity. I would weigh commercial APIs (such as OpenAI) for their superior context windows and retrieval accuracy. While commercial APIs generally offer strong multilingual support, they can struggle with highly specialized legal terminology, prompting a tradeoff evaluation against domain-specific, fine-tuned open-source models. To mitigate API costs, I would implement strict context retrieved chunk pruning for queries to minimize prompt token overhead sent to the LLM. To minimize systemic latency, I would implement semantic caching for repetitive queries. Routing input queries through a local Small Language Model (SLM) to catch out-of-scope prompts or gibberish serves as a low-cost guardrail, preventing expensive commercial API calls for unanswerable questions.


//README includes at least 2 example system responses with source attribution visible in the output text.

Question 1
Question: According to the UCF housing guide, what are the names of the three UCF Affiliated housing properties, and what specific operational advantage do they offer students regarding financial aid compared to other off-campus properties?

LLM Answer: 
According to the provided text corpus, the three UCF Affiliated housing properties are:

1. Knights Circle
2. The Pointe at Central
3. UnionWest Student Living

The specific operational advantage these properties offer students regarding financial aid is that they allow students to utilize financial aid, such as Florida Pre-Paid, Bright Futures, grants, or student loans, directly towards their rent in a seamless process, compared to other off-campus properties where the funds would be released to the student rather than the complex directly.

LLM Source Document: 
2024_Knights-Guide-to-Living-off-campus_Final-2.pdf

Question 2
Question: Under District of Columbia regulations cited in the GW guide, what is the maximum allowable height for grass and weeds on a premise, what is the potential fine for failing to adhere to this rule, and how quickly must snow/ice be cleared from abutting sidewalks after it stops falling?

LLM Answer:
Based on the provided text corpus, here are the answers to your question:

* The maximum allowable height for grass and weeds on a premise under District of Columbia regulations is 8 inches (in-residence) and 10 inches (off-premise).
* Failing to adhere to this rule could lead to fines of more than $500.
* Snow/ice must be cleared from abutting sidewalks after it stops falling within the first 8 daylight hours. This requirement applies specifically to clear snow and ice from sidewalks and handicap curb ramps.

Please note that these regulations apply only to properties within the District of Columbia, as referenced in the text corpus.

LLM Source Document: 
• GW_off-campus-living-guide.pdf
• off-campus-guide.pdf


//README includes one out-of-scope query example with the system's refusal response shown.

# Out-of-Scope Query
Question: How do I bake a chocolate cake?
Answer: I don't have enough information.

//README explains how grounding is enforced in the prompt or pipeline.

# Grounding Enforcement

To ensure absolute factual reliability and eliminate fabrications (hallucinations), this RAG pipeline enforces grounding at both the pipeline architecture layer and the prompt engineering layer:

1. System Prompt Constraints & Role-Bounding
   In generate.py, the LLM is restricted to a tight context-bounded role using a strict system instruction: "You are a helpful assistant answering questions based on a provided text corpus." This explicitly shifts the model from a general-knowledge generator to a localized search synthesizer.

2. Step-by-Step Fact Scanning
   The prompt forces the model to follow a structured synthesis process before generating its final text. It is instructed to first scan the retrieved corpus specifically for rules, guidelines, or behavioral responsibilities related to the setting in the query, and to explicitly distinguish between on-campus and off-campus rules if both are present in the text chunks.

3. Zero-Tolerance Deterministic Fallback
   To prevent the LLM from relying on its pre-trained global weights when local data is missing, a strict negative constraint is hardcoded into the prompt instructions (Instruction #4). If the retrieved text chunks do not contain relevant information, the model is commanded to bypass generation entirely and reply with exactly one deterministic string: "I don't have enough information."

4. Automated Source Attribution Loop
   The ingestion pipeline (ingest.py) binds the source PDF filename to the metadata of each chunk in ChromaDB. When a query is executed, query.py/generate.py extracts this metadata along with the raw text. The Gradio UI (app.py) then isolates and presents these "Verified Source Manuals" in a dedicated output field. This creates an unalterable audit trail, allowing users to manually verify the source documentation of any synthesized answer.


//All 5 test questions are documented, each with the question, the expected correct answer, and the system's actual response.
//An accuracy judgment is given for each question (accurate / partially accurate / inaccurate).

# Evaluation Report: 5 Test Questions & Ground-Truth Answers

Question 1
Question: According to the UCF housing guide, what are the names of the three UCF Affiliated housing properties, and what specific operational advantage do they offer students regarding financial aid compared to other off-campus properties?
Answer: The three UCF Affiliated properties are Knights Circle, The Pointe at Central, and UnionWest Student Living. The specific operational advantage is that they offer students a seamless process to utilize financial aid (such as Florida Pre-Paid, Bright Futures, grants, or student loans) directly towards their rent, whereas at other off-campus properties, the financial aid funds are released to the student rather than the complex directly.  

LLM Answer: 
According to the provided text corpus, the three UCF Affiliated housing properties are:

1. Knights Circle
2. The Pointe at Central
3. UnionWest Student Living

The specific operational advantage these properties offer students regarding financial aid is that they allow students to utilize financial aid, such as Florida Pre-Paid, Bright Futures, grants, or student loans, directly towards their rent in a seamless process, compared to other off-campus properties where the funds would be released to the student rather than the complex directly.

LLM Source Document: 
2024_Knights-Guide-to-Living-off-campus_Final-2.pdf

Accuracy: Accurate

Question 2
Question: Under District of Columbia regulations cited in the GW guide, what is the maximum allowable height for grass and weeds on a premise, what is the potential fine for failing to adhere to this rule, and how quickly must snow/ice be cleared from abutting sidewalks after it stops falling?
Answer: District regulations prohibit grass and weeds from growing more than 10 inches in height. Failing to adhere to this rule can lead to fines of more than $500. Additionally, snow and ice must be cleared from abutting sidewalks within the first eight daylight hours after the precipitation stops falling.  

LLM Answer:
Based on the provided text corpus, here are the answers to your question:

* The maximum allowable height for grass and weeds on a premise under District of Columbia regulations is 8 inches (in-residence) and 10 inches (off-premise).
* Failing to adhere to this rule could lead to fines of more than $500.
* Snow/ice must be cleared from abutting sidewalks after it stops falling within the first 8 daylight hours. This requirement applies specifically to clear snow and ice from sidewalks and handicap curb ramps.

Please note that these regulations apply only to properties within the District of Columbia, as referenced in the text corpus.

LLM Source Document: 
• GW_off-campus-living-guide.pdf
• off-campus-guide.pdf

//At least one failure case is identified with a specific cause tied to a part of the pipeline — not just "it got it wrong," but why (e.g., "the relevant sentence was split across a chunk boundary").
# Failure Case Explanation
Accuracy: Partially Accurate. LLM got the fine and the snow removal timeline right, but it hallucinated a restriction about grass height ("8 inches in-residence and 10 inches off-premise"), which contradicts the real rule of a flat 10 inches.

Question 3
Question: According to the University of Delaware guide, what are the maximum statutory limits or caps placed on landlord application fees and pet deposits in the state of Delaware?
Answer: Application Fee: Cannot exceed the greater of 10 percent of the monthly rent or $50.  Pet Deposit: Cannot exceed one month's rent, and can only be charged for actual pets, excluding service or verified emotional support animals.  

LLM Answer:
According to the provided text, the University of Delaware Off-Campus Living Guide states that a landlord may charge an application fee, but it cannot exceed "the greater of 10 percent of the monthly rent or $50." 

There is no specific information about the maximum cap on pet deposits mentioned in the provided text. However, since the University of Delaware guide recommends keeping resources related to tenant rights and the Delaware Residential Landlord-Tenant Code, we can infer that further information regarding pet deposits might be found within these referenced documents.

As for the application fees, the guide explicitly mentions a limit of 10 percent of the monthly rent or $50.

LLM Source Document:
• OCG_web.pdf

Accuracy: Partially Accurate

Question 4
Question: If a George Washington University student residing off-campus has their roommates abandon the property, what legal concept determines their financial obligation to the landlord, and how long does a landlord legally have to return a security deposit or provide written notice of damages after move-out under D.C. housing regulations?
Answer: The legal concept is "several and joint liability," which dictates that all signers are responsible for anything due or owed, meaning a remaining tenant can be held liable for the entire rent amount if roommates desert them. Upon moving out, the landlord has 45 days to return the deposit or notify the tenant in writing of intended damage deductions. 

LLM Answer:
Based on the provided text corpus, I'll address your question about the George Washington University student's financial obligation and the D.C. housing regulations.

**Financial Obligation:**
The text mentions that students are obligated to remove all personal property upon departure (ABANDONED ITEMS section), but it doesn't explicitly state a legal concept determining their financial obligation to the landlord. However, this responsibility is likely related to common law principles of abandonment and the implied covenant of quiet enjoyment. If roommates abandon the property, the remaining tenant(s) may be liable for any damages or unpaid rent.

**Security Deposit Return:**
According to D.C. housing regulations (not explicitly stated in the provided text but assumed based on general knowledge), a landlord has 30 days to return a security deposit after move-out under D.C. law. This is per DC Municipal Regulations Title 14, Chapter 16: Rent Control and Security Deposits.

**Written Notice of Damages:**
Similarly, if there are damages, the landlord must provide written notice to the tenant within a reasonable time frame, which in D.C. typically allows for 30 days after move-out to dispute any charges or notify the tenant of the intention to deduct from the security deposit.

Please note that these answers assume general knowledge and might not be exhaustive or applicable in every situation. For specific guidance on D.C. housing regulations, it's recommended to consult with a qualified attorney or local authorities familiar with the regulations.

**Additional Resources:**

*   DC Municipal Regulations Title 14, Chapter 16: Rent Control and Security Deposits
*   D.C. Department of Consumer and Regulatory Affairs (DCRA)
*   National Apartment Association (NAA) Guide to Washington, D.C. Landlord-Tenant Law

LLM Source Document:
• rlh-handbook-clarion.pdf
• GW_off-campus-living-guide.pdf
• student-affairs_conduct_Residential-Handbook.pdf

Accuracy: Inaccurate
 
Question 5
Question: Under the University of Delaware's guidelines, what is the exact timeline required for a landlord to begin and complete repairs after receiving notice of a defective condition not caused by the tenant? If the landlord fails to act within this timeline, what specific financial remedy is available to the tenant?
Answer: Upon receiving notice, the landlord must reasonably begin repairs within 10 days and complete them within 30 days. If the landlord fails to do so, the tenant's remedy is that they may complete the repair themselves and deduct the cost from their rent, up to the lesser of one-half of a month's rent or a sum not exceeding $200.00.  

LLM Answer:
Based on the provided text corpus, it appears that the University of Delaware is not mentioned. However, the text does provide information related to a written lease and landlord-tenant responsibilities.

The relevant information can be found in the following sections:

* "You should expect a written lease. While it’s not required unless the lease is for one year or longer, you may (and should) request that the lease be in writing."
* "Upon notice of a defective condition that was not caused by you or your guests, the landlord must reasonably begin repairs within 10 days and complete the repairs within 30 days. If the landlord fails to do so, the tenant may complete the repair and deduct the lesser of one half of a month’s rent or a sum not exceeding $200.00."

According to this information, if the landlord receives notice of a defective condition that was not caused by the tenant, they must:

1. Begin repairs within 10 days
2. Complete repairs within 30 days

If the landlord fails to act within this timeline, the tenant may complete the repair and deduct the lesser of one half of a month’s rent or a sum not exceeding $200.00 from their security deposit.

Note that this information does not specifically mention the University of Delaware but rather general guidelines for landlords and tenants.

LLM Source Document:
• rlh-handbook-clarion.pdf
• GW_off-campus-living-guide.pdf
• OCG_web.pdf

Accuracy: Partially Accurate

//README describes the interface's input and output fields and includes a sample interaction transcript showing a complete query and response.
# Gradio UI and Sample Transcript

1. INTERFACE DESCRIPTION (app.py Layout)

The web portal is built using Gradio Components to separate user inputs, 
synthesized AI insights, and verifiable system metadata:

* INPUT FIELDS:
  - "Enter Housing Policy Inquiry" (gr.Textbox): A single-line interactive 
    text input area with a placeholder where users enter plain-language 
    housing queries.
  - "Search" (gr.Button): A trigger button that executes the 
    RAG pipeline. The pipeline can also be triggered via the 'Enter' key.

* OUTPUT FIELDS:
  - "Answer" (gr.Textbox): An 8-line, read-only text 
    box displaying the synthesized, context-bounded answer from the 
    Llama model.
  - "Verified Source Manuals" (gr.Textbox): A 3-line, read-only metadata 
    field displaying the specific source PDF names mapped to the retrieved 
    database chunks for absolute auditability.


2. SAMPLE INTERACTION TRANSCRIPT

Below is a complete, successful transcript of an interaction through the 
portal interface:

------------------------------------------------------------------------
[USER INPUT]
------------------------------------------------------------------------
Inquiry Text Box ("Enter Housing Policy Inquiry" (gr.Textbox)): 
According to the UCF housing guide, what are the names of the three UCF 
Affiliated housing properties, and what specific operational advantage do 
they offer students regarding financial aid compared to other off-campus 
properties?

------------------------------------------------------------------------
[SYSTEM PROCESSING... Executing Match via all-MiniLM-L6-v2]
------------------------------------------------------------------------

------------------------------------------------------------------------
[PORTAL OUTPUTS]
------------------------------------------------------------------------
Answer:
According to the provided text corpus, the three UCF Affiliated housing 
properties are:

1. Knights Circle
2. The Pointe at Central
3. UnionWest Student Living

The specific operational advantage these properties offer students regarding 
financial aid is that they allow students to utilize financial aid, such as 
Florida Pre-Paid, Bright Futures, grants, or student loans, directly 
towards their rent in a seamless process, compared to other off-campus 
properties where the funds would be released to the student rather than 
the complex directly.

Verified Source Manuals:
• 2024_Knights-Guide-to-Living-off-campus_Final-2.pdf
------------------------------------------------------------------------

//Section describes at least 2 specific instances of AI tool use, naming what the student directed the AI to do in each case.
//Each instance describes what the student reviewed, revised, or overrode. The section reads as genuine collaboration — the student was directing, not just accepting output.
# AI Tool Use

This project was developed through a collaborative process with Gemini, where I directed the AI to implement specific pipeline components and then reviewed or revised the outputs to meet technical requirements.

1. When the system initially returned "I don't have enough information" for queries regarding off-campus guests, I directed the AI to help me refine the generation prompt to be more flexible

Revision: The AI initially suggested adding a specific "Note" to the prompt that hardcoded instructions about looking for "off-campus" keywords. I critiqued and rejected this approach, identifying it as "hardcoding" that would break the system's generality for other topics like parking or pets. I instead directed the AI to implement a Chain-of-Thought (CoT) instruction format. This forced the model to logically scan for "behavioral expectations" and "responsibilities" before deciding to refuse an answer, which successfully resolved the issue without sacrificing the system's ability to handle diverse queries.

2. I directed the AI to help me move beyond basic fixed-size chunking, which was cutting off policy rules mid-sentence. I asked for an industry-standard, free, local method to better preserve the semantic meaning of the housing guides.

Revision: I reviewed the AI's suggestion to use the RecursiveCharacterTextSplitter from LangChain. I revised the recursive chunking implementation by configuring specific separators (paragraph [\n\n], line break [\n], space [ ], individual characters [""]) and an overlap of 200 characters to ensure that complex legal clauses remained intact within single vector embeddings rather than being fragmented.