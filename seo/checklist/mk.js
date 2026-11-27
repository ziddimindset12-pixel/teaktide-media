const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file:///home/claude/seo/checklist/checklist.html');await p.waitForTimeout(300);
await p.pdf({path:'/home/claude/site3/India-Supplier-Verification-Checklist.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close();})();
