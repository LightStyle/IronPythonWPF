import clr
clr.AddReference("System.Xml")
clr.AddReference("PresentationFramework, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")
clr.AddReference("PresentationCore, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")
clr.AddReference('System.Speech')
from System.Speech.Synthesis import SpeechSynthesizer
from System.IO import StringReader, FileStream, FileMode, FileAccess
from System.Xml import XmlReader
from System.Windows.Markup import XamlReader, XamlWriter
from System.Windows import Window, Application

xaml_path = "C:\Users\computer\Documents\Visual Studio 2010\Projects\WpfApplication1\WpfApplication1\main.xaml"

def Waddle(c, d):
    s = str(c.__class__)
    if "System.Windows.Controls." in str(c) and hasattr(c, "Name") and c.Name.Length>0:
        ControlType = s[s.find("'") + 1 : s.rfind("'")]
        if ControlType not in d:
            d[ControlType] = {}
        d[ControlType][c.Name] = c
    if hasattr(c, "Children"):
        for cc in c.Children:
            Waddle(cc, d)
    elif hasattr(c, "Child"):
        Waddle(c.Child, d)
    elif hasattr(c, "Content"):
        Waddle(c.Content, d)

def changeSpeech(s, e):
    t1 = 'Make '
    t2 = 'my '
    t3 = 'pc '
    t4 = 'talk!'
    txt = controls['TextBox']['Text']
    print 'B1' in str(s)
    if 'B1' in str(s):
        txt.Text += t1
    elif 'B2' in str(s):
        txt.Text += t2
    elif 'B3' in str(s):
        txt.Text += t3
    elif 'B4' in str(s):
        txt.Text += t4

def talk(s, e):
    spk = SpeechSynthesizer()
    spk.Speak(controls['TextBox']['Text'].Text)

file = FileStream(xaml_path, FileMode.Open, FileAccess.Read)
xr = XmlReader.Create(file)
win = XamlReader.Load(xr)
controls = {}
Waddle(win, controls)

if __name__ == "__main__":
    for butt in controls['Button']:
        if butt != 'Speak':
            controls['Button'][butt].Click += changeSpeech
    controls['Button']['Speak'].Click += talk

    Application().Run(win)