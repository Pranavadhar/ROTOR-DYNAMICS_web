import gradio as gr


def rotor(FREQUENCY, POWER, VOLTAGE, INERTIA_CONSTANT, P_mech, P_electric):
    strd_KE = INERTIA_CONSTANT * POWER
    angl_freq = 2 * 180 * FREQUENCY
    angl_mom = (2 * INERTIA_CONSTANT * POWER)/angl_freq
    P_accl = P_mech - P_electric
    rotor_Accl = P_accl / angl_mom
    return {
        "STORED KINETIC ENERGY": strd_KE,
        "ANGULAR FREQUENCY": angl_freq,
        "ANGULAR MOMENTUM": angl_mom,
        "ACCELERATING POWER": P_accl,
        "ROTOR ACCELERATION": rotor_Accl
    }


def main(FREQUENCY, POWER, VOLTAGE, INERTIA_CONSTANT, P_mech, P_electric):
    results = rotor(FREQUENCY, POWER, VOLTAGE,
                    INERTIA_CONSTANT, P_mech, P_electric)

    op_components = [
        gr.Number(label="STORED KINETIC ENERGY",
                  value=results["STORED KINETIC ENERGY"]),
        gr.Number(label="ANGULAR FREQUENCY",
                  value=results["ANGULAR FREQUENCY"]),
        gr.Number(label="ANGULAR MOMENTUM",
                  value=results["ANGULAR MOMENTUM"]),
        gr.Number(label="ACCELERATING POWER",
                  value=results["ACCELERATING POWER"]),
        gr.Number(label="ROTOR ACCELERATION",
                  value=results["ROTOR ACCELERATION"])
    ]
    return results["STORED KINETIC ENERGY"], results["ANGULAR FREQUENCY"], results["ANGULAR MOMENTUM"], results["ACCELERATING POWER"], results["ROTOR ACCELERATION"], op_components


op_components = [
    gr.Number(label="STORED KINETIC ENERGY -> UNIT: MI"),
    gr.Number(label="ANGULAR FREQUENCY IN DEGREES"),
    gr.Number(label="ANGULAR MOMENTUM -> UNIT: MJS/electron degree"),
    gr.Number(label="ACCELERATING POWER"),
    gr.Number(label="ROTOR ACCELERATION -> UNIT : (electron degree)/s^2")
]
iface = gr.Interface(
    fn=main,
    inputs=["number", "number", "number", "number", "number", "number"],
    outputs=op_components,
    title="ROTOR DYNAMIC CALCULATOR  - AN ENERGY SYSTEM PROJECT",
    description="THIS IS AN END TO END ENERGY SYSTEM PROJECT DONE TO PERFORM THE ROTOR DYNAMIC CALCULATIONS \n\n"
    "DEPLOYMENT TOOL : GRADIO. \n\n"
    "BASE LANGUAGE : PYHTON \n\n"
)

iface.launch(share=True)
