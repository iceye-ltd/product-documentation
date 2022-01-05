from logging import lastResort
from manim import *
import math
from manim.mobject.svg.svg_path import vector_angle
from manim.utils import scale
from numpy import arctan2

from numpy.typing import _128Bit

# Add some default styles
iceyeWhite       = "#FFFFFF"
iceyeGrey        = "#F1F1F1"
iceyeBlack       = "#000000"
iceyeDarkGrey    = "#555555"
iceyePurple      = "#471D6F"
iceyeLightPurple = "#A42382"
iceyeGreen       = "#71B17F"
iceyeBlue        = "#000046"
iceyeLightBlue   = "#1CB5DF"
iceyeLogo        = ImageMobject("assets/no-border-iceye-logo-black.png").scale(0.25).to_corner(RIGHT+DOWN)

class explainingGeoErrors(Scene):
    '''
    Animation to explain why measuring the geospatial accuracy of a point 
    in a SAR image is critically dependent on the terrain model used in 
    the calculations.

    For dev compile with 
        manim -pql geospatial.py explainingGeoErrors

    For high quality 
        manim -pqh geospatial.py explainingGeoErrors

    To save output as gif 
        manim -pq[l|h] --format=gif geospatial.py explainingGeoErrors
    '''

    def construct(self):
        # Add the iceye logo if needed
        self.add(iceyeLogo)
        satcen =[-5.5,3.0,0.0]
        # sat.scale(0.25).shift(satcen)
        # self.add(sat)
    
        # define some convenience functions
        def setupTerrain():
            terrainPts = [(-4.,-1.01,0.),(-3.5,-0.5,0.),(-3.,-0.5,0.),(-2.6,0.0,0),(-2.2,-0.6,0),(-1.,-1.2,0.)]
            return terrainPts
        
        def lookAngle(p):
            a     = math.sqrt((satcen[0]-p[0])**2 + (satcen[1]-p[1])**2)
            theta = math.acos((R**2 + earth_radius**2 - a**2)/(2*R*earth_radius))
            horiz = math.sin(theta)*earth_radius
            vert = math.cos(theta)*earth_radius
            la = math.asin(np.abs(p[0]-satcen[0])/a)
            return la, a, horiz, vert

        def lookAngleEllipsoid(slantRange,ellipsoidRadius):
            theta = math.acos((R**2 + ellipsoidRadius**2 - slantRange**2)/(2*R*ellipsoidRadius))
            horiz = math.sin(theta)*ellipsoidRadius
            vert  = math.cos(theta)*ellipsoidRadius

            laEllipsoid=math.asin(horiz/slantRange)
            peakPointEllipsoid=[earth_centre[0]+horiz,earth_centre[1]+vert,0]
            return laEllipsoid,peakPointEllipsoid

        def latlontextUpdater(mob) :
            cent=pe3dot.get_center()
            theta= np.arctan2(cent[0]-earth_centre[0],cent[1]-earth_centre[1])
            string='latitude     : %4.1f deg\nlongitude : %4.1f deg'%(np.degrees(theta),np.degrees(theta/2))
            latlonlable.become(Text(string,font_size=24,font='Rajdhani',weight=BOLD,color=iceyeLightBlue).next_to(positionArrow,direction=DOWN))

        # Initialize some common variables
        earth_centre=[-5.5,-51.0,0.0]
        earth_radius=50.0
        R=math.sqrt((satcen[0]-earth_centre[0])**2 + (satcen[1]-earth_centre[1])**2)
        terrainPts = setupTerrain()
        l1,a1,h1,v1 = lookAngle(terrainPts[1])
        l2,a2,h2,v2 = lookAngle(terrainPts[2])
        l3,a3,h3,v3 = lookAngle(terrainPts[3])
        l4,a4,h4,v4 = lookAngle(terrainPts[4])
        le1,pe1 = lookAngleEllipsoid(a1,earth_radius)
        le2,pe2 = lookAngleEllipsoid(a2,earth_radius)
        le3,pe3 = lookAngleEllipsoid(a3,earth_radius)
        le4,pe4 = lookAngleEllipsoid(a4,earth_radius)

        # Title
        sat=ImageMobject("assets/Gen2.png").shift(1.5*UP)
        title1=Text('WHY TERRAIN HEIGHT IS CRITICAL FOR FINDING',font='Rajdhani',weight=BOLD,font_size=40, color=iceyeBlack).shift(DOWN)
        title2=Text('THE POSITION OF A POINT IN A SAR IMAGE',font='Rajdhani',weight=BOLD,font_size=40, color=iceyeBlack).next_to(title1,DOWN)
        title=VGroup(title1,title2)
        self.add(sat,title)
        self.wait(1.5)

        # Radar line to a point - text "Radars just measure range"
        t1 = Text("A RADAR MEASURES RANGE",font='Rajdhani',font_size=36,weight=BOLD, color=iceyeBlack).shift(DOWN)
        self.play(FadeOut(title))
        self.play(GrowFromCenter(t1),sat.animate.move_to(satcen).scale(0.25))
        self.wait(0.5)
        p1 = Dot(terrainPts[1],color=iceyePurple)
        p2 = Dot(terrainPts[2],color=iceyeLightPurple)
        p3 = Dot(terrainPts[3],color=iceyeLightBlue)
        p4 = Dot(terrainPts[4],color=iceyeGreen)
        beam3=Arrow(satcen,p3,color=iceyeLightBlue)
        terrain = VGroup()
        for i in range(len(terrainPts)-1):
            x,y,_ = terrainPts[i]
            xp,yp,_ = terrainPts[i+1]
            terrain.add(Line([x,y,0],[xp,yp,0],color=iceyeDarkGrey))

        self.play(GrowFromCenter(p3))
        pulsearc =  Arc(radius=1,start_angle=-((PI/2)-l3+np.radians(15)),angle=np.radians(30),arc_center=satcen,color=iceyeGreen )
        self.play( pulsearc.animate.move_to(p3), run_time=1 , rate_func=rate_functions.linear)
        arc=pulsearc.rotate(PI)
        self.play( arc.animate.move_to(sat), run_time=1 , rate_func=rate_functions.linear)
        self.remove(arc)
        self.play(GrowArrow(beam3))
        self.wait()

        t2=Text("RANGES ARE STORED IN THE 'SLANT PLANE'",font='Rajdhani',font_size=36,weight=BOLD, color=iceyeBlack).shift(DOWN)
        self.play(FadeOut(t1))
        self.play(FadeIn(t2))

        # Create number line along top
        slantRange = NumberLine(
            x_range=[100, 1000, 100],
            length=10,
            color=iceyeBlue,
            include_numbers=True,
            label_direction=UP,
            font_size=24,
        )
        slantRange.numbers.set_color(iceyeBlack)
        slantRange.move_to(satcen+(1+5)*RIGHT)
        nlLabel = Text("km",font='Rajdhani',font_size=24, color=iceyeBlack).move_to(slantRange,aligned_edge=(DOWN+RIGHT)).shift(0.5*RIGHT)
        srnumlineGroup=VGroup(slantRange,nlLabel).shift(0.2*UP)
        self.bring_to_back(srnumlineGroup)
        self.play(GrowFromCenter(srnumlineGroup),t2.animate.shift(2*DOWN))
        pointGrp = VGroup(p1,p2,p4)
        arc3 = Arc(radius=a3,start_angle=-((PI/2)-l3),angle=(PI/2)-l3,arc_center=satcen,color=iceyeLightBlue)
        self.play(FadeIn(arc3))
        self.bring_to_front(beam3)
        self.play(
            MoveAlongPath(p3, arc3), 
            Rotate(beam3,((PI/2)-l3),about_point=satcen)
        )
        self.play(FadeOut(beam3))
    
        # draw the terrain
        self.play(FadeIn(terrain))
        self.play(FadeIn(pointGrp))
        arc1 = Arc(radius=a1,start_angle=-((PI/2)-l1),angle=(PI/2)-l1,arc_center=satcen,color=iceyePurple)
        arc2 = Arc(radius=a2,start_angle=-((PI/2)-l2),angle=(PI/2)-l2,arc_center=satcen,color=iceyeLightPurple)
        arc4 = Arc(radius=a4,start_angle=-((PI/2)-l4),angle=(PI/2)-l4,arc_center=satcen,color=iceyeGreen)
        self.play(
            MoveAlongPath(p1, arc1),
            MoveAlongPath(p2, arc2),
            MoveAlongPath(p4, arc4),
            run_time=1, rate_func=linear)
        self.play(FadeOut(arc3))
        self.wait()

        
        # text "The radar has no information about where the ground is"
        # Create arc from point 
        # text "the point can be anywhere along this line"
        t3=Text("THE RADAR DOES NOT KNOW WHERE THE GROUND IS",font='Rajdhani',font_size=36,weight=BOLD, color=iceyeBlack).shift(2.5*DOWN)
        self.play(FadeOut(t2))
        self.play(FadeIn(t3))
        arc11=Arc(radius=a1,start_angle=0,angle=-(PI/2),arc_center=satcen,color=iceyeDarkGrey,stroke_width=1)
        arc22=Arc(radius=a2,start_angle=0,angle=-(PI/2),arc_center=satcen,color=iceyeDarkGrey,stroke_width=1)
        arc33=Arc(radius=a3,start_angle=0,angle=-(PI/2),arc_center=satcen,color=iceyeDarkGrey,stroke_width=1)
        arc44=Arc(radius=a4,start_angle=0,angle=-(PI/2),arc_center=satcen,color=iceyeDarkGrey,stroke_width=1)
        self.play(Create(arc11),
            Create(arc22),
            Create(arc33),
            Create(arc44))

        t4a=Text("EACH POINT CAN BE",font='Rajdhani',font_size=32,weight=BOLD, color=iceyeBlack).shift(3*RIGHT+UP)
        t4b=Text("ANYWHERE",font='Rajdhani',font_size=32,weight=BOLD, color=iceyeLightPurple).next_to(t4a,DOWN)
        t4c=Text("ON ITS RANGE ARC",font='Rajdhani',font_size=32,weight=BOLD, color=iceyeBlack).next_to(t4b,DOWN)
        text4grp = VGroup(t4a,t4b,t4c)   
        self.play(FadeIn(text4grp))

        # make a copy of each point and slide them along their arcs and back to terrain
        p11=p1.copy()
        m11=MoveAlongPath(p11, arc11)
        p22=p2.copy()
        m22=MoveAlongPath(p22, arc22)
        p33=p3.copy()
        m33=MoveAlongPath(p33, arc33)
        p44=p4.copy()
        m44=MoveAlongPath(p44, arc44)
        self.play(m11,m22,m33,m44, run_time=1, rate_func=rate_functions.ease_in_out_sine)

        arc111=Arc(radius=a1,start_angle=-(PI/2),angle=l1,arc_center=satcen)
        m111=MoveAlongPath(p11, arc111)
        arc222=Arc(radius=a2,start_angle=-(PI/2),angle=l2,arc_center=satcen)
        m222=MoveAlongPath(p22, arc222)
        arc333=Arc(radius=a3,start_angle=-(PI/2),angle=l3,arc_center=satcen)
        m333=MoveAlongPath(p33, arc333)
        arc444=Arc(radius=a4,start_angle=-(PI/2),angle=l4,arc_center=satcen)
        m444=MoveAlongPath(p44, arc444)
        self.play(m111,m222,m333,m444, run_time=1, rate_func=rate_functions.ease_in_out_sine)
        self.wait()

        self.play(FadeOut(t3),FadeOut(text4grp))
        ellipsoid = Arc(radius=earth_radius,arc_center=earth_centre, start_angle=0, angle=100*DEGREES,color=iceyeGreen)
        self.bring_to_back(ellipsoid)
        labellip = Text('Earth Ellipsoid',font_size=24,font='Rajdhani',weight=BOLD, color=iceyeGreen).shift(5.2*RIGHT+2*DOWN).rotate(np.radians(-12))
        self.play(Create(ellipsoid),FadeIn(labellip))

        t5a=Text("FOR CONVENIENCE IMAGES ARE",font='Rajdhani',font_size=36,weight=BOLD, color=iceyeBlack).shift(3*DOWN)
        t5b=Text("PROJECTED TO A 'GROUND PLANE'",font='Rajdhani',font_size=36,weight=BOLD, color=iceyeBlack).next_to(t5a,DOWN)
        t5=VGroup(t5a,t5b)
        self.play(FadeIn(t5))

        t55a=Text("GROUND PLANE IMAGES ASSUME",font='Rajdhani',font_size=28,weight=BOLD, color=iceyeBlack).shift(3*RIGHT+UP)
        t55b=Text("THAT POINTS ARE ON AN ELLIPSOID",t2c={'[:17]':iceyeBlack,'[17:]':iceyeLightPurple} ,font='Rajdhani',font_size=28,weight=BOLD).next_to(t55a,DOWN)
        t55c=Text("APPROXIMATING THE EARTH'S SURFACE",font='Rajdhani',font_size=28,weight=BOLD, color=iceyeBlack).next_to(t55b,DOWN)
        t55=VGroup(t55a,t55b,t55c)
        self.play(FadeIn(t55))
 
        tc0 =terrain[0].copy()
        tc1 =terrain[1].copy()
        tc2 =terrain[2].copy()
        tc3 =terrain[3].copy()
        tc4 =terrain[4].copy()
        pc1=p11.copy()
        pc2=p22.copy()
        pc3=p33.copy()
        pc4=p44.copy()
        self.play(
            terrain[0].animate.become(Line(terrainPts[0],pe1,color=iceyeDarkGrey,stroke_width=2)),
            p11.animate.become(Dot(pe1,color=iceyePurple)),
            terrain[1].animate.become(Line(pe1,pe2,color=iceyeDarkGrey,stroke_width=2)),
            p22.animate.become(Dot(pe2,color=iceyeLightPurple)),
            terrain[2].animate.become(Line(pe2,pe3,color=iceyeDarkGrey,stroke_width=2)),
            p33.animate.become(Dot(pe3,color=iceyeLightBlue)),
            terrain[3].animate.become(Line(pe3,pe4,color=iceyeDarkGrey,stroke_width=2)),
            p44.animate.become(Dot(pe4,color=iceyeGreen)),
            terrain[4].animate.become(Line(pe4,terrainPts[5],color=iceyeDarkGrey,stroke_width=2)),
            ) 
        self.wait()

        self.play(
            terrain[0].animate.become(tc0),
            p11.animate.become(pc1),
            terrain[1].animate.become(tc1),
            p22.animate.become(pc2),
            terrain[2].animate.become(tc2),
            p33.animate.become(pc3),
            terrain[3].animate.become(tc3),
            p44.animate.become(pc4),
            terrain[4].animate.become(tc4),
            )
        self.play(
            terrain[0].animate.become(Line(terrainPts[0],pe1,color=iceyeDarkGrey,stroke_width=2)),
            p11.animate.become(Dot(pe1,color=iceyePurple)),
            terrain[1].animate.become(Line(pe1,pe2,color=iceyeDarkGrey,stroke_width=2)),
            p22.animate.become(Dot(pe2,color=iceyeLightPurple)),
            terrain[2].animate.become(Line(pe2,pe3,color=iceyeDarkGrey,stroke_width=2)),
            p33.animate.become(Dot(pe3,color=iceyeLightBlue)),
            terrain[3].animate.become(Line(pe3,pe4,color=iceyeDarkGrey,stroke_width=2)),
            p44.animate.become(Dot(pe4,color=iceyeGreen)),
            terrain[4].animate.become(Line(pe4,terrainPts[5],color=iceyeDarkGrey,stroke_width=2)),
            ) 

        self.wait()

        # t6=Text("THIS IS OBSERVED AS 'LAYOVER'",font='Rajdhani',font_size=36, color=iceyeBlack).shift(3*DOWN)
        self.play(FadeOut(t5),FadeOut(t55))
        t7a=Text("A POINT'S TRUE LOCATION CAN ONLY",font='Rajdhani',weight=BOLD,font_size=36, color=iceyeBlack).shift(3*DOWN)
        t7b=Text("BE FOUND USING A TERRAIN MODEL",font='Rajdhani',font_size=36,weight=BOLD, color=iceyeBlack).next_to(t7a,DOWN)
        t7=VGroup(t7a,t7b)
        self.play(FadeIn(t7),FadeOut(VGroup(arc11,arc22,arc44)))

        theta = math.acos((R**2 + earth_radius**2 - a3**2)/(2*R*earth_radius))
        positionArrow = Arc(radius=earth_radius-0.5,arc_center=earth_centre, start_angle=PI/2,
            angle= -theta,color=iceyeLightBlue).add_tip(tip_length=0.15)
        latlonlable=Text('latitude     : %4.1f deg\nlongitude : %4.1f deg'%(np.degrees(theta),np.degrees(theta/2)),
            font_size=24,font='Rajdhani',weight=BOLD,color=iceyeLightBlue).next_to(positionArrow,direction=DOWN)
        self.play(Create(positionArrow),FadeIn(latlonlable))

        tarc=Arc(radius=a3,start_angle=-((PI/2)-le3),angle=l3-le3,arc_center=satcen)
        pe3dot=Dot(pe3,color=iceyeLightBlue)
        self.bring_to_front(pe3dot)
        m3=MoveAlongPath(pe3dot, tarc)
        terrain_radius=math.sqrt((terrainPts[3][0]-earth_centre[0])**2 + (terrainPts[3][1]-earth_centre[1])**2)
        theta_terrain=math.acos((R**2 + terrain_radius**2 - a3**2)/(2*R*terrain_radius))
        newpositionArrow=Arc(radius=earth_radius-0.5,arc_center=earth_centre, start_angle=PI/2,
            angle= -theta_terrain,color=iceyeLightBlue).add_tip(tip_length=0.15)

        latlonlable.add_updater(latlontextUpdater)

        self.play(
            terrain[0].animate.become(tc0),
            FadeOut(p11),
            terrain[1].animate.become(tc1),
            FadeOut(p22),
            terrain[2].animate.become(tc2),
            terrain[3].animate.become(tc3),
            FadeOut(p44),
            terrain[4].animate.become(tc4),
            FadeOut(p1,p2,p4)
            )

        self.wait()

        self.play(
            FadeOut(p33),
            m3,positionArrow.animate.become(newpositionArrow),
            run_time=4)
 
        self.wait()
        
        t8=Text("IF AN INCORRECT TERRAIN IS USED ...",font='Rajdhani',font_size=28,weight=BOLD, color=iceyeBlack).shift(3*RIGHT+UP)
        self.play(FadeIn(t8))


        # incorrectTerrain1 = terrain.copy()
        # terrainPtsCopy = terrainPts.copy()
        # terrainPtsCopy[3] = terrainPtsCopy[3]+UP
        # for i in range(len(terrainPts)-1):
        #     x,y,_ = terrainPtsCopy[i]
        #     xp,yp,_ = terrainPtsCopy[i+1]
        #     incorrectTerrain1.add(Line([x,y,0],[xp,yp,0],color=iceyeDarkGrey))

        wrongpt = terrainPts[3]+UP 
        terrain2cpy=Line(terrain[2].get_start(),terrain[2].get_end(),color=iceyeDarkGrey,stroke_width=1)
        terrain3cpy=Line(terrain[3].get_start(),terrain[3].get_end(),color=iceyeDarkGrey,stroke_width=1)
        self.bring_to_back(terrain2cpy,terrain2cpy)
        self.play(
            terrain2cpy.animate.become(Line(terrain[2].get_start(),wrongpt,color=iceyeDarkGrey,stroke_width=1)),
            terrain3cpy.animate.become(Line(wrongpt,terrain[3].get_end(),color=iceyeDarkGrey,stroke_width=1))
        )

        self.wait()

        earthRadError = math.sqrt((wrongpt[0]-earth_centre[0])**2 + (wrongpt[1]-earth_centre[1])**2)
        lawrongortho,orthowrongpt = lookAngleEllipsoid(a3,earthRadError)
        arcwrongortho = Arc(radius=a3,start_angle=-((PI/2)-l3),angle=lawrongortho-l3,arc_center=satcen)
        theta_terrain=math.acos((R**2 + earthRadError**2 - a3**2)/(2*R*earthRadError))
        newpositionArrow=Arc(radius=earth_radius-0.5,arc_center=earth_centre, start_angle=PI/2,
            angle= -theta_terrain,color=iceyeLightBlue).add_tip(tip_length=0.15)
        self.play(
            terrain2cpy.animate.become(Line(terrain[2].get_start(),orthowrongpt,color=iceyeDarkGrey,stroke_width=1)),
            terrain3cpy.animate.become(Line(orthowrongpt,terrain[3].get_end(),color=iceyeDarkGrey,stroke_width=1)),
            MoveAlongPath(pe3dot, arcwrongortho),
            positionArrow.animate.become(newpositionArrow)
        )

        t9a=Text("...THE COORDINATES OF THE",font='Rajdhani',font_size=28,weight=BOLD, color=iceyeBlack).next_to(t8,DOWN)
        t9b=Text("POINT WILL BE INCORRECT",t2c={'[:11]':iceyeBlack,'[11:]':iceyeLightPurple},font='Rajdhani',font_size=28,weight=BOLD, color=iceyeBlack).next_to(t9a,DOWN)
        t9=VGroup(t9a,t9b)
        self.play(FadeIn(t9))
        self.wait(2)

        self.play(FadeOut(t7,t8,t9))
        t10a = Text("THE GEOSPATIAL ACCURACY OF A SAR",t2c={'[:13]':iceyeBlack,'[13:21]':iceyeLightPurple},font='Rajdhani',font_size=28,weight=BOLD, color=iceyeBlack).shift(3*RIGHT+UP)
        t10b = Text("IMAGE IS THEREFORE A FUNCTION OF THE",font='Rajdhani',font_size=28,weight=BOLD, color=iceyeBlack).next_to(t10a,DOWN)
        t10c = Text("ACCURACY OF THE TERRAIN MODEL USED",t2c={'[:8]':iceyeGreen,'[8:13]':iceyeBlack,'[13:25]':iceyeLightPurple}
            ,font='Rajdhani',font_size=28,weight=BOLD, color=iceyeBlack).next_to(t10b,DOWN)
        self.play(FadeIn(t10a))
        self.play(FadeIn(t10b))
        self.play(FadeIn(t10c))

        terrain_radius=math.sqrt((terrainPts[3][0]-earth_centre[0])**2 + (terrainPts[3][1]-earth_centre[1])**2)
        theta_terrain=math.acos((R**2 + terrain_radius**2 - a3**2)/(2*R*terrain_radius))


        self.play(
            terrain2cpy.animate.become(Line(terrain[2].get_start(),terrainPts[3],color=iceyeDarkGrey,stroke_width=1)),
            terrain3cpy.animate.become(Line(terrainPts[3],terrain[3].get_end(),color=iceyeDarkGrey,stroke_width=1)),
            MoveAlongPath(pe3dot, arcwrongortho.reverse_direction()),
            positionArrow.animate.become(Arc(radius=earth_radius-0.5,arc_center=earth_centre, start_angle=PI/2,
            angle= -theta_terrain,color=iceyeLightBlue).add_tip(tip_length=0.15)),
            run_time=4
        )
        
        # Always finish with a wait
        self.wait()

class radarRange(Scene):
    def construct(self):
        # Add the iceye logo if needed
        self.add(iceyeLogo)
        
        sat=ImageMobject("assets/Gen2.png")
        satcen =[-5.5,3,0]
        tarcen=[5,-2,0]
        sat.scale(0.25).shift(satcen)
        targ=Triangle(color=iceyeBlue).shift(tarcen).scale(0.25)
        angle = math.radians(30)
        arrow = DoubleArrow(satcen,tarcen,color=iceyeDarkGrey,stroke_width=3)
        msecs = 0

        def textUpdater(mob,dt) :
            msecs+=dt
            secstr='time %05.2f ms'%msecs
            mob.become(Text(secstr,font='Rajdhani',font_size=36, color=iceyeLightBlue).move_to(timer))

        timer = Rectangle(width=3.2, height=0.9).to_corner(LEFT+DOWN).set_fill(iceyeDarkGrey,opacity=1.0)
        timerTxt = Text(str(msecs)+' sec',font='Rajdhani',font_size=36, color=iceyeLightBlue).move_to(timer)
        timerTxt.add_updater(textUpdater)

        self.add(sat,targ,timer,timerTxt)
        self.wait(0.5)

        arc =  Arc(color=iceyeGreen, radius=2,angle=angle).move_to(sat).rotate(-45*PI/180)
        self.play( arc.animate.move_to(targ), run_time=2 , rate_func=rate_functions.linear)
        arc=arc.rotate(PI)
        self.play( arc.animate.move_to(sat), run_time=2 , rate_func=rate_functions.linear)
        self.remove(arc)
        timerTxt.remove_updater(textUpdater)
        self.play(FadeIn(arrow))

        speedOfLight = 299792458.0
        dist=299792458.0*msecs/2/1e6
        dtext1 = Text('DISTANCE',font='Rajdhani',weight='BOLD',font_size=40,color=iceyePurple).shift(3*LEFT)

        distText = MathTex(r"\frac{ct}{2}=\frac{3\times10^8 \times %05.2f"%msecs+"}{2}=%7.3fkm"%dist,font_size=40,color=iceyePurple).next_to(dtext1,direction=1.3*DOWN)
        distText.shift(RIGHT)
        self.play(FadeIn(dtext1,distText))

        self.wait(2)
