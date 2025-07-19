import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod/v4";


const server = new McpServer({
    name : "orchestra",
    version : "1.0.0",
    capablities: {
        resources : {},
        tools : {},
        prompt : {}
    }
})



server.tool("create-user","Create a new user in the database",{
    name : z.string(),
    email : z.string(),
    address : z.string()

},{
    title : "create User",
    readOnlyHint: false,
    destructiveHint: false,
    idempotentHint : false,
    openWorldHint : false

},

async (params) => {
        return{}
    }
)



// need to use hhtp streaming
const main = async ()=>{

 const transport = new StdioServerTransport()
 await server.connect(transport)

}

main()