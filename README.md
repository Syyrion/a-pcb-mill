# A-PCB mill

Making PCBs for a hobbyist can be frustrating because of lead times. While it is incredible that we can get high quality PCBs from manufacturers within a week, there are still some significant gripes to contend with.

- **Shipping can be expensive**  
  Sometimes you just want a small, simple PCB which will cost 5 dollars, but then you get a shipping fee of 20 dollars which can make you think twice about whether you really need that PCB.

- **Rapid prototyping is not possible**  
  A one-week lead time is impressive, but can still be too slow. If you need the PCB to continue the project, you really can't do anything for that week until they arrive. If you made a mistake, you then have to repeat the process which can become incredibly time consuming and frustrating. And paying for faster shipping just makes the whole process more expensive.

Our solution to this would be to make a highly accessible and inexpensive PCB mill that almost any mid to high level electronics enthusiast could use. The purpose of this mill would not be to replace purchasing of PCBs from actual manufacturers. This mill would serve as a way to make "draft" PCBs that the user could test and verify before sending the design to a actual manufacturer. (If users are satisfied with the quality of the draft PCBs they could just use those in their projects too if the wish.)

## Disadvantages of Alternatives

- **Nasty chemicals**  
  A low tech way to make PCBs is to mask the traces and etch them using an acid to dissolve away the copper, leaving the traces behind. The masking can be done with a light sensitive photoresist layer on top of the copper that gets removed by a laser or UV light, or some sort of ink that is transferred to the copper. Either way, this is frankly a terrible way to make PCBs. It involves large amounts of chemicals that can be harmful and makes a huge mess. Often the quality of the traces isn't very good and thin traces are very easily destroyed in the process.

- **Other commercial PCB mills**  
  Decent commercial solutions to at-home PCB manufacturing (i.e. mills that are actually marketed as being able to make PCBs) are pretty much aways in the range of about $3000 to over $5000. This is out of reach for almost all hobbyists. 

- **Additive PCB Manufacturing**  
  This involves printing the PCB traces with some sort of conductive paste. Some commercial machines on the market use this technique but it comes with some big downsides:
  
  Additive PCBs are exotic and seem to be meant only for niche experimental use. The manufacturing process differs so much from a normal PCB you'd order from a regular manufacturer that I find it difficult to believe that you could use one to verify your normal designs meant for subtractive manufacturing.
  
  Also, what even is that conductive paste and where would you get it? It's not solder paste but something else that acts as PCB traces. You might be forever chained to buying the materials from the original manufacturer. I'd also bet that their nominal resistance is higher than that of regular copper traces.

# Members

- Ricky Cui (EE 2025)
- Azam Khan (ME 2025)

# Goals

- Rig a 3D printer gantry with an end mill. (What could possibly go wrong?)
  - Test its accuracy and determine feasibility.
  - If we can't make the 3D printer accurate enough, we'll have to find some other solution or a compromise.
- Single layer milling
  - Cut some copper-clad
- Through-hole drilling
- Solder mask scraping
  - Make a custom spring-bit to remove rolled on solder mask to expose pads.

## Stretch goals
- Two layer milling
  - Finding a reliable way to align the two sides well is super important.
- Via insertion?

## Super stretch goals

- Pick-and-Place (PnP) attachment
- Solder paste printer

## Specifications
(We'll figure these out later as we check the feasibility of rigging a 3D printer gantry)

- Minimum track width: ~0.5mm?
- Minimum via size: ???
